# Bulawa landing page (rough mockup)

A single-file mockup of the Bulawa invitations site: hero with a tap-to-open envelope demo,
template gallery with filters, feature grid, pricing, and the order steps.

- `index.html` — open directly in a browser.
- `page.html` — the same page without the document wrapper (used for publishing as a Claude artifact).

WhatsApp and RSVP buttons show a toast; nothing is wired to a backend yet.

## Noor invitation (tap-through)

`noor/index.html` is a full tap-through invitation built on the Noor template:
ten cards (cover, names, invitation, countdown, events, families, story, photos, RSVP, thank you).
Tap the right side or use the arrow keys to move on. The RSVP only shows a confirmation here;
in the live product, replies go to the host. `noor/page.html` is the same page without the document wrapper, for publishing.
