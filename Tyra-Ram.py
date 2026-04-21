#!/usr/bin/env python3

import smtplib
import time
import random
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from colorama import Fore, Style, init

# Initialize colorama
init(autoreset=True)

# ==================== YOUR CREDENTIALS (EDIT HERE) ====================
SENDER_EMAIL = "tyranrootcyber@gmail.com"
SENDER_PASSWORD = "xvwc tkej sigx lcxo"
# =======================================================================

# ==================== MESSAGE BODIES (Randomly Selected) ====================
MESSAGE_BODIES = [
    "⚠️ Your security is an illusion. Your data is now our asset.",
    "🔐 Your systems have been marked. We move in shadows, strike without warning.",
    "💀 Led by ATHEX, we don't make requests—we make statements.",
    "🎯 Ignore this at your own peril. TEAM ATHEX.",
    "🌑 Where others see walls, we see doors.",
    "🔥 Your firewall is just a suggestion. We're already inside.",
    "📡 Your activity has been monitored for the past 30 days.",
    "⚡ This is not a test. Your security has been compromised.",
    "🕷️ We don't break in. We were never locked out.",
    "🎭 Your data is valuable. And now, it's ours.",
    "🔓 Every system has a flaw. We found yours.",
    "📀 Your backups? We already have them too.",
    "⚙️ This message will self-destruct in your mind. Not really.",
    "🎪 Welcome to the dark side. We have cookies. And your passwords.",
    "🔮 We predicted you'd ignore this. That's why we already won."
]

# ==================== SUBJECTS (Randomly Selected) ====================
SUBJECTS = [
    "⚠️ Security Alert",
    "🔐 System Notification",
    "💀 TEAM ATHEX",
    "🎯 Important Message",
    "🌑 Confidential",
    "🔥 Urgent Notice",
    "📡 System Report",
    "⚡ Action Required",
    "🕷️ Security Breach",
    "🎭 Your Data",
    "🔓 Account Update",
    "📀 System Log",
    "⚙️ Maintenance Alert"
]

def generate_random_message():
    """Generate random message from the list"""
    return random.choice(MESSAGE_BODIES)

def generate_random_subject(email_num):
    """Generate random subject"""
    base_subject = random.choice(SUBJECTS)
    return f"{base_subject} [ID: {email_num}]"

def send_emails(recipient_email, num_emails):
    """Send multiple emails with random content"""
    
    print(f"\n{Fore.CYAN}{Style.BRIGHT}[+] Connecting to Gmail SMTP as {SENDER_EMAIL}...{Style.RESET_ALL}")
    
    try:
        server = smtplib.SMTP("smtp.gmail.com", 587)
        server.starttls()
        server.login(SENDER_EMAIL, SENDER_PASSWORD)
        print(f"{Fore.GREEN}{Style.BRIGHT}[✓] Logged in successfully.{Style.RESET_ALL}\n")
    except smtplib.SMTPAuthenticationError:
        print(f"{Fore.RED}{Style.BRIGHT}[❌] Login failed! Please check your Gmail App Password.{Style.RESET_ALL}")
        print(f"{Fore.YELLOW}➡ Make sure 2-Step Verification is ON and you're using an App Password.{Style.RESET_ALL}")
        return
    except Exception as e:
        print(f"{Fore.RED}{Style.BRIGHT}[❌] Could not connect: {e}{Style.RESET_ALL}")
        return

    start_time = time.time()
    success_count = 0
    failed_count = 0

    for i in range(1, num_emails + 1):
        try:
            # Generate random content for each email
            message_body = generate_random_message()
            subject = generate_random_subject(i)
            
            # Create email
            msg = MIMEMultipart()
            msg["From"] = SENDER_EMAIL
            msg["To"] = recipient_email
            msg["Subject"] = subject
            msg.attach(MIMEText(message_body, "plain"))

            # Send email
            server.sendmail(SENDER_EMAIL, recipient_email, msg.as_string())
            success_count += 1
            
            # Show progress with message preview
            preview = message_body[:50] + "..." if len(message_body) > 50 else message_body
            print(f"{Fore.GREEN}[✓] Email {i}/{num_emails} sent{Style.RESET_ALL}")
            print(f"    {Fore.CYAN}Subject:{Fore.WHITE} {subject}{Style.RESET_ALL}")
            print(f"    {Fore.CYAN}Message:{Fore.WHITE} {preview}{Style.RESET_ALL}\n")

            time.sleep(0.15)  # Small delay to avoid rate limiting

        except smtplib.SMTPResponseException as e:
            if e.smtp_code == 421:
                print(f"{Fore.YELLOW}[⚠] Rate limited. Waiting 3 seconds...{Style.RESET_ALL}")
                time.sleep(3)
                failed_count += 1
            else:
                print(f"{Fore.RED}[!] SMTP error: {e.smtp_error}{Style.RESET_ALL}")
                failed_count += 1
        except Exception as e:
            print(f"{Fore.RED}[!] Error: {e}{Style.RESET_ALL}")
            failed_count += 1

    end_time = time.time()
    
    print(f"\n{Fore.CYAN}{Style.BRIGHT}{'='*50}{Style.RESET_ALL}")
    print(f"{Fore.GREEN}[✓] COMPLETED!{Style.RESET_ALL}")
    print(f"{Fore.CYAN}[✓] Total Requested: {num_emails}{Style.RESET_ALL}")
    print(f"{Fore.GREEN}[✓] Successfully Sent: {success_count}{Style.RESET_ALL}")
    print(f"{Fore.RED}[✗] Failed: {failed_count}{Style.RESET_ALL}")
    print(f"{Fore.CYAN}[⏱️] Time taken: {end_time - start_time:.2f} seconds{Style.RESET_ALL}")
    print(f"{Fore.CYAN}{'='*50}{Style.RESET_ALL}")

    server.quit()

def banner():
    """Display professional banner"""
    print(f"{Fore.MAGENTA}{Style.BRIGHT}")
    print("╔══════════════════════════════════════════════════════════════════════════════╗")
    print("║                                                                              ║")
    print("║      ████████╗██╗   ██╗██████╗  █████╗     ██████╗ █████╗ ███╗   ███╗      ║")
    print("║      ╚══██╔══╝╚██╗ ██╔╝██╔══██╗██╔══██╗    ██╔══██╗██╔══██╗████╗ ████║      ║")
    print("║         ██║    ╚████╔╝ ██████╔╝███████║    ██████╔╝███████║██╔████╔██║      ║")
    print("║         ██║     ╚██╔╝  ██╔══██╗██╔══██║    ██╔══██╗██╔══██║██║╚██╔╝██║      ║")
    print("║         ██║      ██║   ██║  ██║██║  ██║    ██║  ██║██║  ██║██║ ╚═╝ ██║      ║")
    print("║         ╚═╝      ╚═╝   ╚═╝  ╚═╝╚═╝  ╚═╝    ╚═╝  ╚═╝╚═╝  ╚═╝╚═╝     ╚═╝      ║")
    print("║                                                                              ║")
    print("║                    ⚡ M A I L S T O R M   P R O   v 1 . 0 ⚡                  ║")
    print("║                        Multi-Message | Random Content                        ║")
    print("║                           Coded by: TyraxZero                               ║")
    print("║                         Educational Purpose Only                            ║")
    print("╚══════════════════════════════════════════════════════════════════════════════╝")
    print(f"{Style.RESET_ALL}")
    print(f"{Fore.YELLOW}{Style.BRIGHT}[!] WARNING: Use only on YOUR OWN email for testing!{Style.RESET_ALL}")
    print(f"{Fore.YELLOW}{Style.BRIGHT}[!] Unauthorized use is ILLEGAL!{Style.RESET_ALL}\n")

def main():
    banner()
    
    recipient_email = input(f"{Fore.CYAN}{Style.BRIGHT}[>] Enter recipient email: {Style.RESET_ALL}").strip()
    
    print(f"\n{Fore.CYAN}{Style.BRIGHT}╔════════════════════════════════════════════════════════════════════════╗{Style.RESET_ALL}")
    print(f"{Fore.CYAN}{Style.BRIGHT}║{Style.RESET_ALL}                         ⚙️  SELECT EMAIL COUNT                      {Fore.CYAN}{Style.BRIGHT}║{Style.RESET_ALL}")
    print(f"{Fore.CYAN}{Style.BRIGHT}╚════════════════════════════════════════════════════════════════════════╝{Style.RESET_ALL}\n")
    
    print(f"  {Fore.GREEN}[1]{Style.RESET_ALL} 10 emails     {Fore.GREEN}[6]{Style.RESET_ALL} 600 emails")
    print(f"  {Fore.GREEN}[2]{Style.RESET_ALL} 50 emails     {Fore.GREEN}[7]{Style.RESET_ALL} 700 emails")
    print(f"  {Fore.GREEN}[3]{Style.RESET_ALL} 100 emails    {Fore.GREEN}[8]{Style.RESET_ALL} 800 emails")
    print(f"  {Fore.GREEN}[4]{Style.RESET_ALL} 200 emails    {Fore.GREEN}[9]{Style.RESET_ALL} 900 emails")
    print(f"  {Fore.GREEN}[5]{Style.RESET_ALL} 500 emails    {Fore.GREEN}[10]{Style.RESET_ALL} 1000 emails")
    print(f"  {Fore.GREEN}[11]{Style.RESET_ALL} Custom number")
    
    choice = input(f"\n{Fore.CYAN}{Style.BRIGHT}[>] Choose (1-11): {Style.RESET_ALL}").strip()
    
    count_map = {
        '1': 10, '2': 50, '3': 100, '4': 200, '5': 500,
        '6': 600, '7': 700, '8': 800, '9': 900, '10': 1000
    }
    
    if choice in count_map:
        num_emails = count_map[choice]
    else:
        num_emails = int(input(f"{Fore.CYAN}{Style.BRIGHT}[>] Enter custom number: {Style.RESET_ALL}").strip())
        if num_emails < 1:
            num_emails = 1
    
    print(f"\n{Fore.RED}{Style.BRIGHT}╔════════════════════════════════════════════════════════════════════════╗{Style.RESET_ALL}")
    print(f"{Fore.RED}{Style.BRIGHT}║{Style.RESET_ALL}                      ⚠️  FINAL WARNING ⚠️                           {Fore.RED}{Style.BRIGHT}║{Style.RESET_ALL}")
    print(f"{Fore.RED}{Style.BRIGHT}╚════════════════════════════════════════════════════════════════════════╝{Style.RESET_ALL}")
    print(f"\n  {Fore.YELLOW}{Style.BRIGHT}📊 Summary:{Style.RESET_ALL}")
    print(f"     From: {Fore.WHITE}{SENDER_EMAIL}{Style.RESET_ALL}")
    print(f"     To: {Fore.WHITE}{recipient_email}{Style.RESET_ALL}")
    print(f"     Emails: {Fore.WHITE}{num_emails}{Style.RESET_ALL}")
    print(f"     Message Mode: {Fore.WHITE}RANDOM (Multi-Message){Style.RESET_ALL}")
    print()
    
    confirm = input(f"{Fore.RED}{Style.BRIGHT}[?] Confirm you own this email? (yes/no): {Style.RESET_ALL}")
    if confirm.lower() != 'yes':
        print(f"\n{Fore.GREEN}[+] Cancelled.{Style.RESET_ALL}")
        return
    
    send_emails(recipient_email, num_emails)

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print(f"\n\n{Fore.YELLOW}{Style.BRIGHT}[!] Stopped by user{Style.RESET_ALL}")
