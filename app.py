import time

def slow_add(x, y):
    print(f"➕ Starting addition of {x} + {y}")
    time.sleep(2)  # simulate delay
    result = x + y
    print(f"✅ Result: {result}")
    return result

def fake_data_processing():
    print("📦 Starting data processing...")
    for i in range(5):
        print(f"🔄 Processing step {i+1}/5...")
        time.sleep(1)  # simulate processing time
    print("✅ Data processing complete!")

def main():
    print("🚀 App Started")
    result = slow_add(10, 5)
    fake_data_processing()
    print("🎉 All tasks complete.")

if __name__ == "__main__":
    main()
