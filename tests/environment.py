from tests.core.web_platform import WebPlatform

def before_all(context):
    """Setup before all tests"""
    context.platform = WebPlatform()
    context.driver = context.platform.start_driver()

def after_all(context):
    """Cleanup after all tests"""
    context.platform.stop_driver()
