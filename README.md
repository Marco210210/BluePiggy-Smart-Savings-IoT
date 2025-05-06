# BluePiggy – IoT Project

**BluePiggy** is an IoT-based smart piggy bank designed to teach kids about saving money while offering parents real-time insights via Telegram and Grafana dashboards.

The system leverages sensors, microcontrollers, and web-based technologies to manage coin detection, locking/unlocking mechanisms, and user notifications through MQTT and REST APIs.

---

## 🌐 Project Overview

- Coin detection and categorization with display feedback.
- Wireless data transmission using MQTT.
- Telegram bot integration for real-time user interaction.
- Grafana dashboard for visualizing statistics.
- Web interface via Altervista for data collection and monitoring.
- Custom-designed pixel-art UI on OLED display.

---

## 🔧 Hardware Components

- **Infrared Sensor (TCRT5000)**: Detects coin passage for automatic value registration.
- **OLED Display (SSD1306 I2C 128×64 px)**: Shows animations, inserted coin value, and updated balance.
- **Servo Motor (SG90 9G)**: Mechanically locks/unlocks the coin compartment via password.
- **AMS1117 Voltage Regulator**: Converts voltage to 3.3V for microcontroller stability.
- **Zerynth Dashboard**: Real-time cloud data aggregation before Grafana visualization.

---

## 🛠️ Technologies & Tools

- **Microcontroller**: Zerynth (Python-like embedded scripting)
- **Protocols**: MQTT, HTTP
- **Backend**: PHP, MySQL (via Altervista)
- **Frontend**: Telegram Bot API, Grafana
- **Design**: Custom .pixil and .png drawings for UI

---

## 📁 Repository Structure

```
BluePiggy-IoT-Project/
├── docs/             → Project reports and slides
├── drawings/         → Pixel-art assets (.pixil, .png)
├── code/             → All project source code
│   ├── Altervista_telegram_Code_Files/
│   ├── Blue_Piggy_Code_Files/
│   ├── MQTT_IDLE_Code_File/
└── README.md
```

---

## 🎬 Video Demo

> 📹 [Watch the BluePiggy demo on YouTube](https://www.youtube.com/watch?v=Uq52akpxfBY&ab_channel=BluePiggy)  

---

## 📄 Documentation

- [BluePiggy - Report (PDF)](docs/Relazione_progetto_IoT_gruppo_18.pdf)
- [Presentation Slides (PPTX)](docs/BluePiggy_presentazione.pptx)

---

## 🚀 How to Run

> Note: This project was developed for an academic IoT course using Zerynth Studio and real hardware components.

1. Review the `code/` directory for main scripts and configurations.
2. Use Zerynth to flash the microcontroller with files in `Blue_Piggy_Code_Files/`.
3. Set up an MQTT broker and connect Telegram bot using your own API token.
4. Use Grafana and Altervista (or any PHP host) to visualize data.

---

## 👥 Contributors

- [Ciancio Vittorio](https://github.com/VittorioCiancio)
- Cuomo Ferdinando
- Di Maio Marco

---