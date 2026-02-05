import asyncio
from adafruit_servokit import ServoKit
kit = ServoKit(channels=16)
async def move_servo(servo_index):
    while True:
        for angle in range(0,90):
            kit.servo[servo_index].angle = angle
            await asyncio.sleep(0.008)
        for angle in range(89,0,-1):
            kit.servo[servo_index].angle = angle
            await asyncio.sleep(0.008)
async def main():
    print("Starting servo movements")
    task1=asyncio.create_task(move_servo(0))
    task2=asyncio.create_task(move_servo(1))
    task3=asyncio.create_task(move_servo(2))
    task4=asyncio.create_task(move_servo(3)) 
    await asyncio.gather(task1,task2,task3,task4)
if __name__ == "__main__":
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        print("\nProgram stopped by user.")
    except Exception as e:
        print(f"An error occurred: {e}")