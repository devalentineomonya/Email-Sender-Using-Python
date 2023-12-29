import ttkbootstrap as tb
from email.message import EmailMessage
import ssl
import smtplib
from tkinter import messagebox
def send_email():
    email_sender = "enter the email address you used to create the app"
    password = "enter your email app password"

    email_reciever = receiver.get()
    subject = subject_entry.get()
    body = body_entry.get("1.0", "end-1c")

    em = EmailMessage()
    em['From'] = email_sender
    em['To'] = email_reciever
    em['Subject'] = subject
    em.set_content(body)

    context = ssl.create_default_context()
    try:
        with smtplib.SMTP_SSL('smtp.gmail.com', 465, context=context) as smtp:
            smtp.login(email_sender, password)
            smtp.sendmail(email_sender, email_reciever, em.as_string())
            messagebox.showinfo("Success", "Email sent successfully!")
    except Exception as e:
        messagebox.showerror("Error", f"Error sending email: {str(e)}")


def cancel_email():
    app.destroy()


app = tb.Window(themename="superhero")
app.title("Email sender with python")
app.geometry("500x700")
screen_width = app.winfo_screenwidth()
screen_height = app.winfo_screenheight()
window_width = 500
window_height = 700

x_position = (screen_width - window_width) // 2
y_position = (screen_height - window_height) // 2

# Set the window position to always center
app.geometry(f"{window_width}x{window_height}+{x_position}+{y_position}")
email_frame = tb.Frame(app, width=380)
email_frame.pack()

#INPUT SECTION

receiver = tb.Entry(email_frame, style="success.TEntry", width=100)
receiver.insert(0, "Enter receiver email")
subject_entry = tb.Entry(email_frame, style="primary.TEntry", width=100)
subject_entry.insert(0, "Enter email subject")
body_entry = tb.Text(email_frame, width=50, height=15, wrap="word", borderwidth=2, relief="solid", highlightthickness=1)
body_entry.insert("1.0", "Enter email body")

#BUTTONS SECTION

send = tb.Button(email_frame, text="SEND", width=100, bootstyle="success", command=send_email)
cancel = tb.Button(email_frame, text="CANCEL", width=100, bootstyle="danger",command=cancel_email)

receiver.pack(pady=(100, 10), padx=50)
subject_entry.pack(pady=10, padx=50)
body_entry.pack(pady=20, padx=50)
send.pack(pady=10, padx=50)
cancel.pack(pady=10, padx=50)




app.mainloop()
