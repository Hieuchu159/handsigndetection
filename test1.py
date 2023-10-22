import h5py
try:
    with h5py.File('Model/keras_model.h5', 'r') as f:
        pass
    print("Tệp hợp lệ")
except Exception as e:
    print("Tệp không hợp lệ hoặc bị hỏng. Lỗi:", str(e))