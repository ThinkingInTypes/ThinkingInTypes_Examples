# basic_lambda_form.py
from book_utils import Catch

with Catch() as catch:
    catch(lambda: 1 / 0)
    catch(lambda: 1 / 0)
    catch(lambda: 1 / 0)
    print("No lambda aborts the context:")
    _ = 1 / 0
    print("This doesn't run:")
    catch(lambda: 1 / 0)
## Error: division by zero
## Error: division by zero
## Error: division by zero
## No lambda aborts the context:
## Error: division by zero
