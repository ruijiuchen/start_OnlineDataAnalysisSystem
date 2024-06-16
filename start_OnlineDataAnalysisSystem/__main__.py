import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QLineEdit, QPushButton, QVBoxLayout, QHBoxLayout, QMessageBox
import subprocess
import toml
import os
class CommandWithParameters(QWidget):
    def __init__(self, label_texts, button_text, command_function, button_color, config_file, parent=None):
        super().__init__(parent)
        self.label_texts = label_texts
        self.button_text = button_text
        self.command_function = command_function
        self.button_color = button_color
        self.config_file = config_file
        
        self.initUI()
        self.load_parameters()
        
    def initUI(self):
        main_layout = QVBoxLayout()
        
        self.param_entries = []
        for label_text in self.label_texts:
            h_layout = QHBoxLayout()
            param_label = QLabel(label_text)
            h_layout.addWidget(param_label)
            param_entry = QLineEdit(self)
            h_layout.addWidget(param_entry)
            self.param_entries.append(param_entry)

            # Add edit button for Parameter field
            if "Parameter" in label_text:
                edit_button = QPushButton("Edit", self)
                edit_button.clicked.connect(lambda _, entry=param_entry: self.edit_parameter(entry))
                h_layout.addWidget(edit_button)
                
                                                                                        
            main_layout.addLayout(h_layout)
            
        self.run_button = QPushButton(self.button_text, self)
        self.run_button.clicked.connect(self.run_command)
        self.run_button.setStyleSheet(f"background-color: {self.button_color}; color: white;")
        main_layout.addWidget(self.run_button)
        
        self.setLayout(main_layout)
            
    def run_command(self):
        params = [entry.text() for entry in self.param_entries]
        try:
            self.save_parameters(params)  # Save parameters before running the command
            self.execute_command(params)            
        except Exception as e:
            QMessageBox.critical(self, "Error", f"An exception occurred: {str(e)}")
            
    def load_parameters(self):
        if os.path.exists(self.config_file):
            with open(self.config_file, 'r') as file:
                config = toml.load(file)
                for entry, value in zip(self.param_entries, config.get("parameters", [])):
                    entry.setText(value)

    def save_parameters(self, params):
        config = {"parameters": params}
        with open(self.config_file, 'w') as file:
            toml.dump(config, file)
            
    def auto_save_parameters(self):
        params = [entry.text() for entry in self.param_entries]
        self.save_parameters(params)                

    def edit_parameter(self, param_entry):
        param_file = param_entry.text()
        if os.path.exists(param_file):
            subprocess.Popen(['xdg-open', param_file])  # This works for Linux. Use 'open' for macOS and 'start' for Windows.
        else:
            QMessageBox.critical(self, "Error", f"File {param_file} does not exist.")
            
        
    def execute_command(self, params):
        try:
            Hostname = params[0]
            Directory = params[1]
            Environment = params[2]
            Program = params[3]
            Parameter = params[4]
            ssh_command = [
                "ssh", "-X", Hostname,
                "xterm", "-hold", "-e",
                f"bash -i -c \"cd {Directory} && conda {Environment} && {Program} {Parameter}\""
            ]
            subprocess.Popen(ssh_command)
        except Exception as e:
            QMessageBox.critical(None, "Error", f"An exception occurred: {str(e)}")                        
    
def run_commands_queqiao_NTCAP(params):
    try:
        Hostname    = params[0]
        Directory   = params[1]
        Environment = params[2]
        Program     = params[3]
        Parameter   = params[4]
        ssh_command = [
            "ssh", "-X", Hostname,
            "xterm", "-hold", "-e",
            f"bash -i -c \"cd {Directory} && conda {Environment} && {Program} {Parameter}\""
        ]
        subprocess.Popen(ssh_command)
    except Exception as e:
        QMessageBox.critical(None, "Error", f"An exception occurred: {str(e)}")
        
def run_commands_analyze_iq_sc(params):
    try:
        hostname = params[0]
        print(" hostname ",hostname)
        ssh_command = [
            "ssh", "-X", hostname,
            "xterm", "-hold", "-e",
            "bash -c \"cd /lustre/astrum/experiment_data/2024-05_E018/OnlineDataAnalysisSystem/analyze_iq_sc && conda activate iqt7_env_ruijiu && analyze_iq_sc ../parameters/analyze_E142exp.toml\""
        ]
        subprocess.Popen(ssh_command)
    except Exception as e:
        QMessageBox.critical(None, "Error", f"An exception occurred: {str(e)}")

def run_combine_injection(params):
    print(params)
    try:
        hostname       = params[0]
        file_dir       = params[1]
        file_start     = params[2]
        file_stop      = params[3]
        average_number = params[4]
        fre_min        = params[5]
        fre_range      = params[6]
        date_start     = params[7]
        ssh_command = [
            "ssh", "-X", hostname,
            "xterm", "-hold", "-e",
            f"bash -i -c 'cd /lustre/astrum/experiment_data/2024-05_E018/OnlineDataAnalysisSystem/combine_injection && conda activate iqt7_env_ruijiu && combine_injection combine_tdms {file_dir} {file_start} {file_stop} {average_number} {fre_min} {fre_range} \"{date_start}\"\'"
        ]
        subprocess.Popen(ssh_command)
    except Exception as e:
        QMessageBox.critical(None, "Error", f"An exception occurred: {str(e)}")

def run_commands_queqiao_RSA(params):
    try:
        hostname = params[0]
        print(" hostname ",hostname)
        ssh_command = [
            "ssh", "-X", hostname,
            "xterm", "-hold", "-e",
            "bash -c \"cd /lustre/astrum/experiment_data/2024-05_E018/OnlineDataAnalysisSystem/RSA && /u/litv-exp/mambaforge/bin/queqiao ../parameters/queqiaosettings_rsa.toml\""
        ]
        subprocess.Popen(ssh_command)
    except Exception as e:
        QMessageBox.critical(None, "Error", f"An exception occurred: {str(e)}")
        
        
def main():
    app = QApplication(sys.argv)
    main_window = QWidget()
    main_window.setWindowTitle("Online data analysis system for IMS experiment")
    main_window.setGeometry(100, 100, 1300, 400)
    
    layout = QVBoxLayout()

    # Create parameter sections
    param_layout = QHBoxLayout()
    hostname_command_ntcap = CommandWithParameters(
        label_texts=["Hostname:","Directory:","Environment:","Program:","Parameter:"],
        button_text="Copy data from NTCAP hard disk to server",
        command_function=run_commands_queqiao_NTCAP,
        button_color="blue",
        config_file="ntcap_params.toml"
    )
    param_layout.addWidget(hostname_command_ntcap)
    
    hostname_command_analyze_iq_sc = CommandWithParameters(
        label_texts=["Hostname:","Directory:","Environment:","Program:","Parameter:"],
        button_text="Convert IQ data to frequency data.",
        command_function=run_commands_analyze_iq_sc,
        button_color="green",
        config_file="analyze_iq_sc_params.toml"
    )
    param_layout.addWidget(hostname_command_analyze_iq_sc)
    
    combine_injection_command = CommandWithParameters(
        label_texts=["Hostname:","Directory:","Environment:","Program:","Parameter:"],
        button_text="Run combine_spectrum",
        command_function=run_combine_injection,
        button_color="red",
        config_file="combine_injection_params.toml"
    )
    param_layout.addWidget(combine_injection_command)
    
    hostname_command_queqiao_RSA = CommandWithParameters(
        label_texts=["Hostname:","Directory:","Environment:","Program:","Parameter:"],
        button_text="Copy data from RSA hard disk to server",
        command_function=run_commands_queqiao_RSA,
        button_color="purple",
        config_file="rsa_params.toml"
    )
    param_layout.addWidget(hostname_command_queqiao_RSA)

    layout.addLayout(param_layout)

    # Add buttons at the bottom
    button_layout = QHBoxLayout()
    button_layout.addWidget(hostname_command_ntcap.run_button)
    button_layout.addWidget(hostname_command_analyze_iq_sc.run_button)
    button_layout.addWidget(combine_injection_command.run_button)
    button_layout.addWidget(hostname_command_queqiao_RSA.run_button)
    
    layout.addLayout(button_layout)
                                
    main_window.setLayout(layout)
    main_window.show()
    
    sys.exit(app.exec_())
    
if __name__ == "__main__":
    main()
