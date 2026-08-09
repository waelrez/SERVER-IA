# REAL AI SERVER

A Python-based AI server with:

- Flask API
- AI processing module
- Memory system
- SQLite database
- CORS support
- Environment configuration

## API

### Health

GET `/health`

### Process

POST `/api/process`

Example:

```json
{
  "text": "Hello AI"
}
