# HubSpot to LinkedIn Auto-Connect with GPT-4o

This workflow automates sending personalized LinkedIn connection requests using contact data from HubSpot CRM and GPT-4o to craft a short message.

---

## What this workflow does

1. **Fetch HubSpot Contact**  
   - Retrieves name, job title, company, and LinkedIn URL from HubSpot CRM.  

2. **Generate Personalized LinkedIn Note**  
   - Uses GPT-4o to write a <300 character note focused on value (no greetings or sign-offs).  

3. **Send LinkedIn Request Automatically**  
   - Uses Puppeteer to open the profile, click "Connect", add the note, and send the invitation.  
   - Takes a debug screenshot during the process.  

---

## Tools and Integrations

- **HubSpot CRM** — contact source  
- **OpenAI GPT-4o** — AI message generation  
- **Puppeteer** — browser automation to send the invitation  

---

## Why I built this

Manually writing and sending LinkedIn requests for every new HubSpot lead is repetitive.  
This workflow automates it end-to-end, saving time and ensuring messages stay personalized and relevant.

---

## Files

- `hubspot_linkedin_autoconnect.json` — workflow export for Make.com or n8n  
- `linkedin_utils.py` — helper script to clean and validate LinkedIn URLs  
- `hubspot_linkedin_autoconnect.png` — screenshot showing the workflow in action  

---

## How to use

1. Import `hubspot_linkedin_autoconnect.json` into Make.com or n8n.  
2. Replace connections (`areeshausmani93_connection`) with your own HubSpot and OpenAI credentials.  
3. Run the workflow to automatically send personalized LinkedIn connection requests.  

---

## Future improvements

- Add error-handling for failed LinkedIn interactions  
- Automatically update HubSpot when a request is sent  
- Extend to support other CRMs (Zoho, Salesforce)
