import torch

# Check if CUDA (GPU support) is available
if torch.cuda.is_available():
    # Get the number of available GPUs
    gpu_count = torch.cuda.device_count()
    print(f"Number of available GPUs: {gpu_count}")
    
    # Print GPU information
    for i in range(gpu_count):
        print(f"\nGPU {i}:")
        print(f"Name: {torch.cuda.get_device_name(i)}")
        print(f"Memory: {torch.cuda.get_device_properties(i).total_memory / 1024**3:.2f} GB")
        
    # Test a simple tensor operation on GPU
    device = torch.device("cuda:0")
    a = torch.randn(3, 3).to(device)
    b = torch.randn(3, 3).to(device)
    c = torch.matmul(a, b)
    print("\nMatrix multiplication result (should be on GPU):")
    print(c)
    
    # Verify it's on GPU
    print(f"\nIs tensor on GPU? {c.is_cuda}")
else:
    print("CUDA is not available. Check your NVIDIA GPU and driver installation.")