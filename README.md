# CocoWatch — CCTV AI Video Analyzer (YOLOv8)

Pequeño proyecto en **Python** que analiza vídeo mp4 (El objetivo es analizar diréctamente cámaras CCTV) y detecta objetos usando **YOLOv8 (Ultralytics)**.
Incluye una UI simple en pantalla con:

- FPS en tiempo real
- Conteo de **Person / Dog / Cat**
- Control de **velocidad** del vídeo (x0.1 → x16) y pausa

> Proyecto funcional en estado actual, subido como demostración de detección y overlay de métricas.

## Demo (captura)

<p align="center">
  <img src="assets/screenshot.png" width="850">
</p>

---

## Controles

- `q` → salir
- `ESPACIO` → pausar/reanudar
- `d` → acelerar
- `a` → ralentizar

---

## Requisitos

- Python 3.10+ recomendado
- OpenCV
- Ultralytics (YOLOv8)

### Uso
Guarda en la carpeta data el archivo de video que quieres analizar.
Pipenv para entornos aislados:
```bash
pip install pipenv
pipenv install
pipenv run python src/main.py --video_name [nombre_archivo.mp4]
