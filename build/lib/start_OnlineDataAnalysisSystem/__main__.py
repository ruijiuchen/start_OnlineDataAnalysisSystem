import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QLineEdit, QPushButton, QVBoxLayout, QHBoxLayout, QMessageBox
import subprocess


class HostnameCommand(QWidget):
    def __init__(self, label_text, button_text, command_function, hostname_required=True, parent=None):
        super().__init__(parent)
        self.label_text = label_text
        self.button_text = button_text
        self.command_function = command_function
        self.hostname_required = hostname_required
        
        self.initUI()
        
    def initUI(self):
        main_layout = QVBoxLayout()
        
        # Horizontal layout for label and entry
        h_layout = QHBoxLayout()
        
        self.hostname_label = QLabel(self.label_text)
        h_layout.addWidget(self.hostname_label)
        
        self.hostname_entry = QLineEdit(self)
        h_layout.addWidget(self.hostname_entry)
        
        main_layout.addLayout(h_layout)
        
        self.run_button = QPushButton(self.button_text, self)
        self.run_button.clicked.connect(self.run_command)
        main_layout.addWidget(self.run_button)
    
        self.setLayout(main_layout)
                                                                                                        
    def run_command(self):
        hostname = self.hostname_entry.text()
        try:
            self.command_function(hostname)
        except Exception as e:
            QMessageBox.critical(self, "Error", f"An exception occurred: {str(e)}")
            
def run_commands_queqiao_NTCAP(hostname):
    try:
        ssh_command = [
            "ssh", "-X", hostname,
            "xterm", "-hold", "-e",
            "bash -i -c \"cd /lustre/astrum/experiment_data/2024-05_E018/OnlineDataAnalysisSystem/ && cd queqiao && source /u/litv-exp/mambaforge/etc/profile.d/conda.sh && conda activate iqt7_env_ruijiu && /u/litv-exp/mambaforge/bin/queqiao ../parameters/queqiaosettings_E143Exp_simulation.toml\""
        ]
        subprocess.Popen(ssh_command)
    except Exception as e:
        QMessageBox.critical(None, "Error", f"An exception occurred: {str(e)}")
        
def run_commands_queqiao_RSA(hostname):
    try:
        ssh_command = [
            "ssh", "-X", hostname,
            "xterm", "-hold", "-e",
            "bash -c \"cd /lustre/astrum/experiment_data/2024-05_E018/OnlineDataAnalysisSystem/ && cd RSA && queqiao ../parameters/queqiaosettings_rsa.toml\""
        ]
        subprocess.Popen(ssh_command)
    except Exception as e:
        QMessageBox.critical(None, "Error", f"An exception occurred: {str(e)}")
        
def run_commands_analyze_iq_sc(hostname):
    try:
        ssh_command = [
            "ssh", "-X", hostname,
            "xterm", "-hold", "-e",
            "bash -c \"cd /lustre/astrum/experiment_data/2024-05_E018/OnlineDataAnalysisSystem/ && cd analyze_iq_sc && conda activate iqt7_env_ruijiu && analyze_iq_sc ../parameters/analyze_E142exp.toml\""
        ]
        subprocess.Popen(ssh_command)
    except Exception as e:
        QMessageBox.critical(None, "Error", f"An exception occurred: {str(e)}")
        
def main():
    app = QApplication(sys.argv)
    main_window = QWidget()
    main_window.setWindowTitle("Online data analysis system for IMS experiment")
    main_window.setGeometry(100, 100, 400, 300)
    
    layout = QVBoxLayout()
    
    hostname_command_ntcap = HostnameCommand(
        label_text="Enter hostname for NTCAP:",
        button_text="Copy data from NTCAP hard disk to server",
        command_function=run_commands_queqiao_NTCAP
    )
    layout.addWidget(hostname_command_ntcap)

    hostname_command_analyze_iq_sc = HostnameCommand(
        label_text="Enter hostname",
        button_text="Convert IQ data to frequency data.",
        command_function=run_commands_analyze_iq_sc,
        hostname_required=False
    )
    layout.addWidget(hostname_command_analyze_iq_sc)
    
    hostname_command_queqiao_RSA = HostnameCommand(
        label_text="Enter hostname",
        button_text="Copy data from RSA hard disk to server",
        command_function=run_commands_queqiao_RSA,
        hostname_required=False
    )
    layout.addWidget(hostname_command_queqiao_RSA)
    
                    
    main_window.setLayout(layout)
    main_window.show()
    
    sys.exit(app.exec_())
    
if __name__ == "__main__":
    main()
                                                                                                                                                                                                                                                                                                                    
