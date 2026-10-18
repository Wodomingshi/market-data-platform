# Decision log

## 2026-10-18: Project setup
- Created private repo `market-data-platform` with a Python .gitignore.
- Chose GitHub Codespaces as the online dev environment.
- Next: fetch US CPI from the FRED API, with the key stored as a secret.

## 2026-10-18: First working pipeline (FRED to Postgres)

**Built**
- Private GitHub repo `market-data-platform`, developed in GitHub Codespaces.
- `src/fred.py`: fetches a FRED series (`fetch_series`) and converts values to numbers, skipping and reporting missing ones (`clean_observations`).
- `src/db.py`: writes rows to Postgres (`save_observations`).
- `src/load.py`: runs fetch, clean and save for one series.
- `sql/001_create_macro_observations.sql`: table definition.
- `requirements.txt`: Python packages the project needs.
- Free Neon Postgres database with table `macro_observations`.
- Loaded 32 monthly US unemployment (`UNRATE`) observations; running the load twice still gives 32 rows.

**Key choices and why**
| Choice | Why |
|---|---|
| FRED API version 1 | We need single series, not bulk release downloads |
| Neon over Supabase | Plain Postgres; as far as I know, it wakes itself after idle periods (to verify) |
| Long table (`series_id`, `obs_date`, `value`) | Indicators have different frequencies; adding one needs no schema change |
| Primary key on (`series_id`, `obs_date`) with `ON CONFLICT DO NOTHING` | Makes loads repeatable without duplicates |
| `NUMERIC` for values | Exact decimals, no float rounding |
| Keys and the database URL stored as Codespaces secrets | Nothing sensitive in code or repo |
| Error message prints the status code only | FRED's default error text would include the URL with the key |
| Missing values (`"."`) skipped and reported, not hidden | Found 2025-10-01 missing for `UNRATE`, which I believe is due to the 2025 shutdown (to confirm on FRED) |
| SQL kept in files under `sql/` | The table design is recorded in the repo, not only in the database |

**Next**
- Basic SQL queries on the loaded data (select, filter, sort, aggregate).
- Check Neon's free-tier limits on its pricing page.
- Load more series (CPI and the rest of the macro list).
- Choose a source for daily US equity prices.