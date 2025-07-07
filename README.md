# 📧 Email Scraper – Extracteur d’adresses email

Ce script Python extrait automatiquement les adresses email depuis une page web.

---

## 🔧 Fonctionnalités

- Récupération automatique des emails depuis une URL
- Résultat sous forme de liste sans doublons
- Facile à utiliser et à modifier
- Adapté aux petits projets de prospection ou de scraping léger

---

## 🧰 Technologies utilisées

- `Python`
- `requests` pour accéder au contenu de la page
- `re` (Regex) pour extraire les emails

---

## 🧪 Exemple d’utilisation

```python
url = "https://example.com"
emails = extract_emails_from_url(url)
for email in emails:
    print(email)
