# Bulawa site

Static site, no build tools. Deploy the `site/` folder as is.

| URL | File | What it is |
| --- | --- | --- |
| `/` | `index.html` | Bulawa landing page (rough mockup) |
| `/wedding` | `wedding/index.html` | Picker for the sample invitations |
| `/wedding/noor` | `wedding/noor/index.html` | Noor: burgundy and cream florals, gatefold doors, petals |
| `/wedding/zardozi` | `wedding/zardozi/index.html` | Zardozi: traditional red and gold Nikah scroll, twirling couple, Sheesh Mahal venue |
| `/wedding/shahi` | `wedding/shahi/index.html` | Shahi: a gold line-drawn palace in ruby, gold dust |

## Editing

Each page has a `page.html` (the copy published as a Claude artifact) and an `index.html`
(the same page wrapped for hosting, with link-preview tags for WhatsApp). Edit `page.html`,
then rebuild the wrappers from the repo root:

```
python3 scripts/build_pages.py
```

`wedding/index.html` is hand-written and has no `page.html`.

## Deploying to Vercel

Either:

- **Import from GitHub:** in Vercel, Add New → Project → import this repo, set **Root Directory** to `site`,
  leave the framework as **Other** with no build command, and deploy. Every push then redeploys.
- **From the command line:** with a Vercel token in `VERCEL_TOKEN`, run
  `npx vercel deploy site --prod --yes --token "$VERCEL_TOKEN"`.

`vercel.json` turns on clean URLs (`/wedding/noor` rather than `/wedding/noor/index.html`), and
`.vercelignore` keeps the `page.html` copies and this README out of the deployment.

Every template lights up where you tap, labels the tap target, and shows "Scroll down" until the guest
first scrolls. The Zardozi venue photo is by Gpkp, CC BY-SA 4.0, via Wikimedia Commons (cropped).

RSVP and Add to Calendar work without a backend: the RSVP shows a confirmation only, and the
calendar buttons open Google Calendar or Outlook with the event filled in.
