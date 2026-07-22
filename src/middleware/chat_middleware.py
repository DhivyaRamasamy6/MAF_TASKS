import os
from dotenv import load_dotenv
load_dotenv()
import re
from cryptography.fernet import Fernet
from collections.abc import Awaitable,Callable
from agent_framework import ChatContext,ChatMiddleware,ChatResponse,ChatResponseUpdate,chat_middleware
from src.common.logger import get_logger
logger=get_logger(__name__)

FERNET_KEY = os.getenv("FERNET_KEY")
# Global counters to keep track of model calls
NON_STREAMING_CALL_COUNT=0
STREAMING_CALL_COUNT=0

class TokenLoggingMiddleware(ChatMiddleware):
    """
    Middleware that logs token usage for both
    streaming and non-streaming LLM responses.
    """
    logger.info("[TokenLoggingMiddleware] processing")
    async def process(
        self,
        context: ChatContext,
        call_next: Callable[[], Awaitable[None]],
    ) -> None:
        global NON_STREAMING_CALL_COUNT,STREAMING_CALL_COUNT
        #handle streaming response
        if context.stream:
            STREAMING_CALL_COUNT+=1
            call_number=STREAMING_CALL_COUNT
            usage_seen_in_updates=False
            def capture_usage_update(update:ChatResponseUpdate)->ChatResponseUpdate:
                nonlocal usage_seen_in_updates
                
                for content in update.contents:
                    if content.type=="usage":
                        usage_seen_in_updates=True
                        print(f"\n[Streaming model call #{call_number}] Usage update:{content.usage_details}")
                return update
            def capture_final_usage(result:ChatResponse)->ChatResponse:
                if not usage_seen_in_updates and result.usage_details:
                    print(f"\n[Streaming model call #{call_number}] Final Usage:{result.usage_details}")
            context.stream_transform_hooks.append(capture_usage_update)
            context.stream_result_hooks.append(capture_final_usage)
            await call_next()
            return
        #handle non streaming response
        NON_STREAMING_CALL_COUNT+=1
        call_number=NON_STREAMING_CALL_COUNT
        await call_next()
        response=context.result
        if isinstance(response,ChatResponse) and response.usage_details:
            print(f"[Non-streaming model call #{call_number}] Usage:{response.usage_details}")
        logger.info("[TokenLoggingMiddleware] processed")
    
@chat_middleware
async def pii_masking_middlewalre(context:ChatContext,call_next,):
    """
    Detects PII in incoming messages, encrypts it, and replaces the
    original values before the request is sent to the LLM.
    """
    logger.info('[pii_masking_middlewalre] processing')
    #cipher 
    cipher=Fernet(FERNET_KEY.encode())
    PII_PATTERNS={
        "AADHAR":r"\b\d{4}\s?\d{4}\s?\d{4}\b",
        "PAN":r"\b[A-Z]{5}[0-9]{4}[A-Z]\b",
    }
    
    for message in context.messages:
        if not message.text:
            continue
        text=message.text
        for pii_type, pii_pattern in PII_PATTERNS.items():
            matches=re.findall(pii_pattern,text)
            for value in matches:
                encrypted=cipher.encrypt(value.encode()).decode()
                text=text.replace(value,encrypted)
                print(f"{pii_type} -> {encrypted}")
        
        text = message.text
    logger.info("[pii_masking_middlewalre] processed")
       
    await call_next()