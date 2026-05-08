import torch
import time
import sys

def generate_mandelbrot(size=8192, max_iters=200):
    device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')
    print("="*60)
    print(f" PyTorch Mandelbrot Benchmark ")
    print("="*60)
    print(f"Using device: {device}")
    
    if device.type == 'cuda':
        print(f"GPU Name: {torch.cuda.get_device_name(0)}")
        print(f"CUDA Version: {torch.version.cuda}")
    else:
        print("WARNING: CUDA not available! Running on CPU will be extremely slow.")
        
    print(f"\nGenerating {size}x{size} fractal with {max_iters} iterations max...")
    
    # Pre-allocate tensors on device
    # Mapping coordinates [-2.0, 1.0] x [-1.5, 1.5]
    x = torch.linspace(-2.0, 1.0, size, device=device)
    y = torch.linspace(-1.5, 1.5, size, device=device)
    
    X, Y = torch.meshgrid(x, y, indexing='ij')
    c = torch.complex(X, Y)
    z = torch.zeros_like(c)
    
    iters = torch.zeros((size, size), dtype=torch.int32, device=device)
    
    start_time = time.time()
    
    for i in range(max_iters):
        # Only compute points that haven't escaped (abs(z) <= 2.0)
        mask = torch.abs(z) <= 2.0
        z[mask] = z[mask]**2 + c[mask]
        iters[mask] += 1
        
    if device.type == 'cuda':
        torch.cuda.synchronize()
        
    end_time = time.time()
    duration = end_time - start_time
    
    print(f"\nGeneration completed in {duration:.4f} seconds!")
    print(f"Total points calculated: {size * size:,}")
    print(f"Performance: {(size * size) / duration / 1e6:.2f} Mega-pixels per second")
    
    # Create an ASCII art representation of the center for fun
    print("\n--- ASCII Fractal Snapshot ---")
    small_size = 60
    step = size // small_size
    sample = iters[::step, ::step].cpu().numpy()
    
    chars = " .:-=+*#%@"
    
    for i in range(min(small_size, sample.shape[0])):
        line = ""
        for j in range(min(small_size, sample.shape[1])):
            val = sample[i, j]
            # Normalize to char length
            idx = int((val / max_iters) * (len(chars) - 1))
            line += chars[idx]
        print(line)
        
    print("\nSuccess! PyTorch GPU execution completed.")

if __name__ == "__main__":
    generate_mandelbrot()
