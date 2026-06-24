# k

Сайт для автоматической загрузки архива с ответами.

GitHub Pages: откройте репозиторий → Settings → Pages → Deploy from branch `main` / folder `/ (root)`.

При переходе на сайт сразу скачивается `answers.zip`.

## Содержимое архива

- `otvety_na_test.txt` — ответы на тест из docx
- `situacionnye_zadachi.txt` — ответы на 10 ситуационных заданий

## Пересборка zip

```bash
python build_zip.py
```
