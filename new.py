 import execjs

def execute_js_code(js_code):
    try:
        ctx = execjs.compile(js_code)
        result = ctx.call("your_function_name")  # Call a specific function in the JavaScript code
        print(result)
    except execjs.RuntimeError as e:
        print(f"An error occurred while executing JavaScript code: {e}")

# Example JavaScript code
js_code = """
function your_function_name() {
    // JavaScript code here
    var message = "Hello from JavaScript!";
    return message;
}
"""

execute_js_code(js_code)
