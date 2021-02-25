import numpy as np

# def _numerical_gradient_no_batch(f, x):
#     h = 1e-4 # 0.0001
#     grad = np.zeros_like(x) # x와 형상이 같은 배열을 생성
    
#     for idx in range(x.size):
#         tmp_val = x[idx]
        
#         # f(x+h) 계산
#         x[idx] = float(tmp_val) + h
#         fxh1 = f(x)
        
#         # f(x-h) 계산
#         x[idx] = tmp_val - h 
#         fxh2 = f(x) 
        
#         grad[idx] = (fxh1 - fxh2) / (2*h)
#         x[idx] = tmp_val # 값 복원
        
#     return grad


# def numerical_gradient(f, X):
#     if X.ndim == 1:
#         return _numerical_gradient_no_batch(f, X)
#     else:
#         grad = np.zeros_like(X)
        
#         for idx, x in enumerate(X):
#             grad[idx] = _numerical_gradient_no_batch(f, x)
        
#         return grad

def numerical_gradient(f, x):
    h = 1e-4 # 0.0001
    grad = np.zeros_like(x)
    
    it = np.nditer(x, flags=['multi_index'], op_flags=['readwrite'])
    while not it.finished:
        idx = it.multi_index
        tmp_val = x[idx]
        x[idx] = float(tmp_val) + h
        fxh1 = f(x) # f(x+h)
        
        x[idx] = tmp_val - h 
        fxh2 = f(x) # f(x-h)
        grad[idx] = (fxh1 - fxh2) / (2*h)
        
        x[idx] = tmp_val # 값 복원
        it.iternext()   
        
    return grad
