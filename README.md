# DGB Infinity - Background Script para Render.com

Script en Python que mantiene el sistema de carreras de caballos funcionando 24/7 en Render.com

## Instalación en Render

### Paso 1: Preparar el repositorio

1. Copia estos archivos a tu repositorio GitHub:
   - `background_races.py`
   - `requirements.txt`
   - `README.md` (este archivo)

2. Haz push a GitHub:
```bash
git add .
git commit -m "Add background races script for Render"
git push origin main
```

### Paso 2: Conectar a Render

1. Ve a https://dashboard.render.com
2. Click en "New +" → "Background Worker"
3. Conecta tu repositorio GitHub
4. Configura así:

**Name:** `horse-racing-background`

**Runtime:** `Python 3`

**Build Command:** `pip install -r requirements.txt`

**Start Command:** `python background_races.py`

**Environment Variables:**
```
PYTHON_VERSION=3.11
```

5. Click en "Create Background Worker"

### Paso 3: Verificar que funciona

- Ve a los logs en Render
- Deberías ver: "=== Script iniciado en Render ==="
- El script estará activo 24/7

## ¿Cómo funciona?

1. El script en Render corre constantemente
2. Verifica que el sistema de carreras esté activo
3. Las carreras se crean en tu hosting (dgb-infinity.wuaze.com)
4. Los usuarios apuestan normalmente en `horse_racing.php`
5. Los resultados se procesan automáticamente

## Costos

**GRATIS** ✅
- Render.com ofrece un worker gratuito por cuenta
- Sin límite de horas
- Sin tarjeta de crédito requerida

## Notas importantes

⚠️ El hosting gratuito de Render puede "dormir" si no hay tráfico en 15 días
✅ Pero tu hosting (wuaze.com) seguirá activo siempre
✅ El script solo verifica/monitorea, no consume muchos recursos

## Troubleshooting

**El script no inicia:**
- Revisa los logs en Render
- Asegúrate que `requirements.txt` está en el repo
- Revisa que la URL sea correcta: `http://dgb-infinity.wuaze.com`

**Las carreras no se crean:**
- Verifica que el script `background_races.php` esté en tu hosting
- Revisa los logs del hosting

**¿Preguntas?**
- Revisa los logs en Render Dashboard
- Verifica la conexión a tu hosting
