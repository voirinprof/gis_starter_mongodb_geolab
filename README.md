# 🧪 GIS Starter: MongoDB + Python + DevContainer

This repository provides a ready-to-use development environment to start working with **MongoDB**, **Python**, and **geospatial data** using **DevContainers** (for VS Code or GitHub Codespaces).

It also includes **Mongo Express** for easy web-based database exploration.

---

## 🚀 Features

- 🐍 Python environment (with `pymongo`)
- 🍃 MongoDB server (with authentication)
- 🌐 Mongo Express for GUI-based DB inspection
- 🐳 Docker + Docker Compose integration
- 💻 VS Code DevContainer support

---

## 📁 Project Structure

```
.
├── .devcontainer/
│   ├── Dockerfile
│   ├── requirements.txt
│   ├── devcontainer.json
│   └── docker-compose.yml
├── scripts/
│   └── ...         # Generates and inserts random geospatial points
│
└── README.md
```

---

## ⚙️ Getting Started

### 📦 Requirements

- [Docker](https://www.docker.com/)
- [Visual Studio Code](https://code.visualstudio.com/) with the **Dev Containers** extension  
  _or use [GitHub Codespaces](https://github.com/features/codespaces)_

### ✅ Steps

1. Clone the repository:
   ```bash
   git clone https://github.com/voirinprof/gis_starter_mongodb_geolab.git
   cd gis_starter_mongodb_geolab
   ```

2. Open in VS Code and select **"Reopen in Container"**

3. Once inside the container, run the script:
   ```bash
   python app/generate_points.py
   ```

4. Open Mongo Express in your browser:
   ```
   http://localhost:8081
   ```
   > Default credentials:
   > - **Username**: `admin`
   > - **Password**: `admin`

Or use `foward port` in the VS Code (codespaces), this is the `8081`.
---

## 🌍 Example Data

The `generate_points.py` script inserts 10 random geospatial points into MongoDB:

```json
{
  "location": {
    "type": "Point",
    "coordinates": [2.3522, 48.8566]
  },
  "description": "Random point #1"
}
```

An automatic `2dsphere` index is created to support spatial queries.

---

## 📌 Notes

- All services run in containers managed by Docker Compose.
- You can use Mongo Express to inspect collections and test spatial data.

---

## 🧭 Future Ideas

- Add example `$geoNear` or `$geoWithin` queries
- Add map-based viewer (e.g., Folium, Kepler.gl)
- Add REST API (with FastAPI or Flask)

---

## 🤝 Contributing

Contributions are welcome! Feel free to open an issue or submit a pull request to improve the setup.
