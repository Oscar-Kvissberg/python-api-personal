# Göteborgs Hamn Data Collector

Detta är Python-scriptet för att hämta data från Göteborgs hamn.

## Installation

```bash
cd python-scripts
pip install -r requirements.txt
```

## Användning

### Lokal utveckling
```bash
python data_collector.py
```

### Som API server
```bash
python main.py
```

## Miljövariabler

Skapa en `.env` fil i `python-scripts/` mappen:

```env
PORT_API_KEY=din_api_nyckel_här
```

## Struktur

- `data_collector.py` - Huvudscript för data collection
- `main.py` - FastAPI server
- `requirements.txt` - Python dependencies
- `startup.sh` - Azure deployment script

## Integration med Next.js

Scriptet kan användas på två sätt:

1. **Lokal utveckling**: Kör Python script separat och använd mock data i Next.js
2. **Produktion**: Deploya Python som separat API och anropa från Next.js

## Vercel Deployment

För Vercel deployment, rekommenderas att Python backend körs separat (t.ex. på Railway, Heroku, eller AWS).

## Framtida Projekt Struktur

För att lägga till fler projekt på din sida, kan du skapa separata mappar:

```
personal-mac/
├── app/
│   ├── Data_analysis/Gbg/     # Nuvarande Göteborgs projekt
│   ├── Project2/              # Framtida projekt
│   └── Project3/              # Framtida projekt
python-scripts/
├── Gbg-API/
│   ├── data_collector.py
│   └── main.py
├── Project2/
│   ├── data_collector.py
│   └── main.py
├── venv/
├── azure-deploy.md
├── README.md
├── requirements.txt
├── startup.sh
├── startup.txt
```

### Exempel på nytt projekt:
1. Skapa ny mapp: `python-scripts-project2/`
2. Kopiera struktur från `python-scripts/`
3. Anpassa `data_collector.py` och `main.py`
4. Skapa ny Next.js sida i `app/Project2/`
5. Deploya till ny Azure Web App

### Fördelar med denna struktur:
- ✅ **Separat** - Varje projekt har sin egen Python backend
- ✅ **Skalbar** - Lätt att lägga till nya projekt
- ✅ **Enkel** - Samma struktur för alla projekt
- ✅ **Flexibel** - Olika Azure Web Apps för olika projekt 