# 🌽 Maizteca - Estudio de Mercado

Análisis de mercado para un proyecto de venta de elotes, basado en datos de encuestas sobre preferencias del consumidor.

## 📊 Descripción

Este proyecto presenta un análisis detallado de un estudio de mercado para evaluar la viabilidad de un negocio de venta de elotes. Utilizando datos recopilados de encuestas, exploramos diversos aspectos del interés y las preferencias del consumidor.

## 🎯 Objetivos del Análisis

- Identificar frecuencia de consumo de elotes
- Analizar lugares de compra preferidos
- Evaluar sabores y combinaciones más populares
- Determinar rangos de precios aceptables
- Entender preferencias de presentación y cocción

## 📁 Estructura del Proyecto

```
maizteca_analisis/
├── main.ipynb           # Notebook principal con análisis
├── data/
│   └── maizteca.csv     # Datos de la encuesta (60 respuestas)
├── assets/
│   └── fonts/           # Fuentes personalizadas para visualizaciones
├── scripts/
│   ├── validate_data.py # Validación de calidad del dataset
│   └── generate_summary.py # Resumen ejecutivo automático
├── reports/
│   └── executive-summary.md # Se genera automáticamente
├── .github/workflows/
│   └── data-quality.yml # CI para validación
└── README.md
```

## 📋 Variables del Dataset

| Variable | Descripción |
|----------|-------------|
| `Marca temporal` | Fecha/hora de respuesta |
| `sexo` | Género del encuestado |
| `edad` | Rango de edad |
| `gusto elote` | Preferencia por elotes |
| `condimentos favoritos` | Toppings preferidos |
| `precio` | Rango de precio dispuesto a pagar |
| `formato presentacion` | Formato de elote preferido |
| `intolerante lactosa` | Intolerancia a lácteos |
| `grado de coccion` | Preferencia de cocción |

## 🚀 Requisitos

```bash
pip install pandas matplotlib jupyter
```

## 💻 Uso

1. Clona el repositorio:
   ```bash
   git clone https://github.com/Chere3/maizteca_analisis.git
   cd maizteca_analisis
   ```

2. Instala dependencias:
   ```bash
   pip install -r requirements.txt
   ```

3. Corre validaciones de calidad:
   ```bash
   make validate
   ```

4. Genera resumen ejecutivo en markdown:
   ```bash
   make summary
   ```

5. Abre el notebook:
   ```bash
   jupyter notebook main.ipynb
   ```

## ✅ Calidad y reproducibilidad

- `make validate`: valida columnas requeridas y missing values del dataset
- `make summary`: crea `reports/executive-summary.md` con hallazgos clave
- GitHub Actions ejecuta `make check` en cada push/PR

## 📈 Visualizaciones Incluidas

- Distribución demográfica de encuestados
- Frecuencia de consumo
- Preferencias de condimentos
- Análisis de precios
- Preferencias de presentación

## 🔬 Metodología

1. **Recolección de datos**: Encuesta digital con 60 participantes
2. **Limpieza de datos**: Validación y normalización con pandas
3. **Análisis exploratorio**: Estadísticas descriptivas
4. **Visualización**: Gráficos con Matplotlib y fuentes personalizadas
5. **Conclusiones**: Recomendaciones basadas en hallazgos

## 📌 Hallazgos Clave

> Los resultados específicos están documentados en el notebook `main.ipynb`

## 🤝 Contribuir

1. Fork el repositorio
2. Crea una rama: `git checkout -b mejora/nueva-visualizacion`
3. Commit cambios: `git commit -m 'feat: agregar gráfico de tendencias'`
4. Push: `git push origin mejora/nueva-visualizacion`
5. Abre un Pull Request

## 📜 Licencia

MIT © [Chere3](https://github.com/Chere3)

---

<p align="center">
  Hecho con 🌽 y Python
</p>
