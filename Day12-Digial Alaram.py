import time
from datetime import datetime, timedelta
import threading
import sys

alarms = []

def display_banner():
    banner = """
    ╔══════════════════════════════════════════╗
    ║     ⏰  D I G I T A L   A L A R M  ⏰    ║
    ║          C L O C K   2 0 2 5             ║
    ╚══════════════════════════════════════════╝
    """
    print(banner)

def check_alarm(alarm_time, recurring=False):
    while True:
        current_time = time.strftime('%H:%M')
        if current_time == alarm_time:
            for _ in range(5):
                print(f"""
                🔔 ALARM TIME! 🔔
                ⏰ WAKE UP! ⏰
                🌟 IT'S {alarm_time}! 🌟
                """)
                time.sleep(0.5)
            if not recurring:
                break
            else:
                alarm_time = (datetime.strptime(alarm_time, '%H:%M') + timedelta(days=1)).strftime('%H:%M')
        time.sleep(1)

def set_alarm():
    try:
        print("\n⏰ Setting New Alarm...")
        alarm_time = input("Enter alarm time (HH:MM format): ")
        datetime.strptime(alarm_time, '%H:%M')  # Validate time format
        recurring = input("Do you want this alarm to recur daily? (yes/no): ").strip().lower() == 'yes'
        alarms.append({'time': alarm_time, 'recurring': recurring})
        print(f"\n✓ Alarm successfully set for {alarm_time} {'(Recurring)' if recurring else ''}")
        alarm_thread = threading.Thread(target=check_alarm, args=(alarm_time, recurring))
        alarm_thread.daemon = True
        alarm_thread.start()
    except ValueError:
        print("\n✗ Invalid time format! Please use HH:MM")

def view_alarms():
    if not alarms:
        print("\nNo alarms set.")
    else:
        print("\nCurrent Alarms:")
        for i, alarm in enumerate(alarms, start=1):
            print(f"{i}. {alarm['time']} {'(Recurring)' if alarm['recurring'] else ''}")

def delete_alarm():
    view_alarms()
    if alarms:
        try:
            alarm_index = int(input("\nEnter the number of the alarm to delete: ")) - 1
            if 0 <= alarm_index < len(alarms):
                removed_alarm = alarms.pop(alarm_index)
                print(f"\n✓ Alarm for {removed_alarm['time']} {'(Recurring)' if removed_alarm['recurring'] else ''} deleted.")
            else:
                print("\n✗ Invalid selection.")
        except ValueError:
            print("\n✗ Please enter a valid number.")

def display_time():
    current_time = time.strftime('%H:%M:%S')
    hour = int(time.strftime('%H'))

    if hour < 12:
        greeting = "Good Morning! 🌅 Rise and Shine!"
    elif hour < 17:
        greeting = "Good Afternoon! 🌞 Stay Productive!"
    else:
        greeting = "Good Evening! 🌙 Time to Relax!"

    border = "♦" * 50
    print(f"\n{border}")
    print(greeting)
    print(f"\n🕐 Current Time: {current_time}")
    print(f"📅 Date: {time.strftime('%d-%m-%Y')}")
    print(f"\n{border}")

def display_menu():
    menu = """
    ╭───── MENU OPTIONS ─────╮
    │                        │
    │  1. 🔔 Set an alarm    │
    │  2. 📋 View alarms     │
    │  3. ❌ Delete an alarm │
    │  4. 🚪 Exit            │
    │                        │
    ╰────────────────────────╯
    """
    print(menu)

def main_menu():
    while True:
        display_banner()
        display_time()
        display_menu()

        choice = input("\nEnter your choice (1-4): ")

        if choice == '1':
            set_alarm()
        elif choice == '2':
            view_alarms()
        elif choice == '3':
            delete_alarm()
        elif choice == '4':
            print("\nGoodbye! 👋 Have a great day!")
            sys.exit()
        else:
            print("\n✗ Invalid choice! Please try again.")

        input("\nPress Enter to continue...")

if __name__ == "__main__":
    try:
        main_menu()
    except KeyboardInterrupt:
        print("\nGoodbye! 👋")
        sys.exit()
