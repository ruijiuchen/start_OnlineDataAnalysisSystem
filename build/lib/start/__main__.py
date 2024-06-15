import tkinter as tk
from tkinter import messagebox
import subprocess

def run_commands_queqiao_NTCAP():
    try:
        ssh_command = [
            "ssh", "-X", "lxir131",
            "xterm", "-hold", "-e",
            "bash -c \"cd /lustre/astrum/experiment_data/2024-05_E018/OnlineDataAnalysisSystem/ && cd queqiao && conda activate iqt7_env_ruijiu && queqiao ../parameters/queqiaosettings_E143Exp_simulation.toml\""
        ]
        subprocess.Popen(ssh_command)
    except Exception as e:
        messagebox.showerror("Error", f"An exception occurred: {str(e)}")
        
def run_commands_queqiao_RSA():
    try:
        ssh_command = [
            "ssh", "-X", "lxir131",
            "xterm", "-hold", "-e",
            "bash -c \"cd /lustre/astrum/experiment_data/2024-05_E018/OnlineDataAnalysisSystem/ && cd RSA && queqiao ../parameters/queqiaosettings_rsa.toml\""
        ]
        subprocess.Popen(ssh_command)
    except Exception as e:
        messagebox.showerror("Error", f"An exception occurred: {str(e)}")
        
def run_commands_analyze_iq_sc():
    try:
        ssh_command = [
            "ssh", "-X", "lxbk0494",
            "xterm", "-hold", "-e",
            "bash -c \"cd /lustre/astrum/experiment_data/2024-05_E018/OnlineDataAnalysisSystem/ && cd analyze_iq_sc && conda activate iqt7_env_ruijiu && analyze_iq_sc ../parameters/analyze_E143Exp_simulation.toml\""
        ]
        subprocess.Popen(ssh_command)
    except Exception as e:
        messagebox.showerror("Error", f"An exception occurred: {str(e)}")
                            
def main():
    # Create the GUI window
    root = tk.Tk()
    root.title("Online data analysis system for IMS experiment")
    root.geometry("300x250")

    # Add a button to execute the commands
    run_button_queqiao_NTCAP = tk.Button(root, text="Copy data from NTCAP hard disk to server", command=run_commands_queqiao_NTCAP)
    run_button_queqiao_NTCAP.pack(pady=(20, 10))

    
    # Add a button to execute the commands
    run_button_analyze_iq_sc = tk.Button(root, text="Convert IQ data to freqnency data.", command=run_commands_analyze_iq_sc)
    run_button_analyze_iq_sc.pack(pady=(10, 20))
    
    # Add a button to execute the commands
    run_button_queqiao_RSA = tk.Button(root, text="Copy data from RSA hard disk to server", command=run_commands_queqiao_RSA)
    run_button_queqiao_RSA.pack(pady=(20, 10))
    
    # Run the GUI main loop
    root.mainloop()
    
if __name__ == "__main__":
    main()
