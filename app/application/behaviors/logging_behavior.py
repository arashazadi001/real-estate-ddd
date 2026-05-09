import time
from app.application.mediator.interfaces import IPipelineBehavior
from app.shared.result.result import Result

class LoggingBehavior(IPipelineBehavior):
    async def handle(self, request, next_call):
        request_name = type(request).__name__
        print(f"--- [LOG] Starting Request: {request_name} ---")
        
        start_time = time.time()
        result = await next_call() # رفتن به مرحله بعدی (یا لایه بعدی یا هندلر)
        duration = time.time() - start_time
        
        status = "Success" if result.is_success else f"Failed ({result.error})"
        print(f"--- [LOG] Finished {request_name} in {duration:.2f}s | Status: {status} ---")
        
        return result
