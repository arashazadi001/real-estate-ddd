from typing import Dict, Type, Any, List, Callable, Awaitable
from app.application.mediator.interfaces import IRequest, IRequestHandler, IPipelineBehavior
from app.shared.result.result import Result

class Mediator:
    def __init__(self):
        self._handlers: Dict[Type[IRequest], IRequestHandler] = {}
        self._behaviors: List[IPipelineBehavior] = []

    # این متد برای ثبت دستی (مثل قبل)
    def register_handler(self, request_type: Type[IRequest], handler: IRequestHandler):
        self._handlers[request_type] = handler

    # --- بخش جدید: Decorator برای ثبت خودکار ---
    def handler(self, request_type: Type[IRequest]):
        """دکوراتور برای ثبت خودکار هندلرها"""
        def decorator(handler_class: Type[IRequestHandler]):
            # ایجاد یک نمونه از هندلر و ثبت آن
            self.register_handler(request_type, handler_class())
            return handler_class
        return decorator
    
    # بقیه متدها (add_behavior و send) بدون تغییر باقی می‌مانند...

    def add_behavior(self, behavior: IPipelineBehavior):
        """افزودن یک لایه جدید به خط لوله (Pipeline)"""
        self._behaviors.append(behavior)

    async def send(self, request: IRequest[Any]) -> Result[Any]:
        request_type = type(request)
        handler = self._handlers.get(request_type)

        if not handler:
            return Result.failure(f"No handler registered for {request_type.__name__}")

        # زنجیر کردن رفتارها (Pipeline Chain)
        async def handle_request():
            return await handler.handle(request)

        # ساختن زنجیره از آخر به اول
        chain = handle_request
        
        # لایه‌ها را به ترتیب عکس دورِ هندلر می‌پیچیم
        for behavior in reversed(self._behaviors):
            # برای حفظ closure، مقدار فعلی chain را به یک متغیر دیگر می‌دهیم
            current_chain = chain
            
            # یک تابع جدید می‌سازیم که لایه فعلی را اجرا می‌کند
            async def wrapped_behavior(b=behavior, c=current_chain):
                return await b.handle(request, c)
            
            chain = wrapped_behavior

        try:
            return await chain()
        except Exception as e:
            return Result.failure(f"System Error: {str(e)}")

mediator = Mediator()
