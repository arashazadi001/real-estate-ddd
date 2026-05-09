from app.application.mediator.interfaces import IPipelineBehavior
from app.shared.result.result import Result

class ValidationBehavior(IPipelineBehavior):
    async def handle(self, request, next_call):
        # در اینجا در آینده کدهای ولیدیشن خودکار قرار می‌گیرد
        print(f"🔍 [VALIDATION] Checking request: {type(request).__name__}")
        
        # اگر مشکلی نبود، برو بعدی
        return await next_call()
