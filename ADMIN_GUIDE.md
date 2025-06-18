# Portfolio Website - Admin Guide

## Overview
Your portfolio website now has dynamic content management through Django Admin Panel. You can easily add, edit, and manage your Education, Experience, and Projects without touching any code.

## Accessing Admin Panel
1. Go to: `http://127.0.0.1:8000/admin/` (or your domain/admin/)
2. Login with your superuser credentials
3. You'll see four main sections: About Me, Education, Experiences, and Projects

## Managing Content

### 👤 About Me Section
**Location:** Admin Panel → About Me

**Fields:**
- **Title:** Section heading (e.g., "Who am I?", "About Me")
- **Description:** Your personal bio/description
- **Photo:** Your profile photo for the about section
- **Is Active:** Check to show on website

**Important Notes:**
- Only ONE About Me entry can be active at a time
- When you activate a new About entry, the previous one is automatically deactivated
- You cannot delete the last remaining About entry
- If no photo is uploaded, a placeholder will be shown

**Tips:**
- Keep description engaging but concise (2-3 paragraphs work best)
- Use high-quality photos (recommended: 400x400 pixels or larger)
- Update regularly to keep your profile current

### 📚 Education Section
**Location:** Admin Panel → Education

**Fields:**
- **Degree:** Your degree name (e.g., "MSc-CS", "BSc (Hons) in Computer Science")
- **Institution:** University/College name
- **Period:** Time period (e.g., "2020 - 2023", "2023 - Present")
- **Description:** Additional details about the degree (optional)
- **Order:** Display order (lower numbers appear first)
- **Is Active:** Check to show on website

**Tips:**
- Use Order field to control the sequence of education items
- Uncheck "Is Active" to temporarily hide an education entry

### 💼 Experience Section
**Location:** Admin Panel → Experiences

**Fields:**
- **Title:** Job title (e.g., "Data Science Intern")
- **Company:** Company/Organization name
- **Period:** Employment period (e.g., "Jan 2024 - May 2024")
- **Responsibilities:** Job responsibilities (enter each on a new line)
- **Order:** Display order (lower numbers appear first)
- **Is Active:** Check to show on website

**Tips:**
- Enter each responsibility on a separate line in the Responsibilities field
- They will automatically appear as bullet points on the website

### ⭐ Daily Horoscopes Section
**Location:** Admin Panel → Daily Horoscopes

**Fields:**
- **Zodiac Sign:** Select from 12 zodiac signs (Aries to Pisces)
- **Date:** Date for this horoscope prediction
- **Description:** Main horoscope prediction text
- **Lucky Number:** Lucky number (1-99)
- **Lucky Color:** Lucky color name
- **Lucky Time:** Lucky time (e.g., 9am, 2pm)
- **Mood:** Today's mood (Excellent, Good, Positive, etc.)
- **Compatibility:** Best compatibility sign (optional)
- **Is Active:** Check to show on website

**Important Notes:**
- Only ONE horoscope per zodiac sign per date is allowed
- Users will see the most recent active horoscope for their sign
- If no horoscope exists for today, the system shows the latest available

**Tips:**
- Update horoscopes daily for fresh content
- Use positive, encouraging language in descriptions
- Vary lucky numbers, colors, and times for authenticity
- Keep descriptions 2-3 sentences for optimal reading
- Content is completely managed by you - no external API dependencies

**Admin Actions:**
- **Duplicate for Today:** Copy selected horoscopes to today's date
- **Mark Active/Inactive:** Bulk activate or deactivate horoscopes

### 🚀 Projects Section
**Location:** Admin Panel → Projects

**Fields:**
- **Title:** Project name
- **Description:** Brief project description
- **Image:** Project screenshot/image (upload from your computer)
- **Demo Link:** Live demo URL (optional) - opens in new tab
- **Code Link:** Source code URL (e.g., GitHub) - opens in new tab
- **Technologies:** Technologies used (comma-separated)
- **Category:** Project category (e.g., "Web App", "Mobile App", "IoT")
- **Order:** Display order (lower numbers appear first)
- **Is Featured:** Check to highlight this project
- **Is Active:** Check to show on website

**Tips:**
- Both Demo Link and Code Link are optional
- If no links are provided, "Links coming soon" will be displayed
- Technologies should be comma-separated (e.g., "Python, Django, JavaScript")
- Upload images in common formats (JPG, PNG, GIF)

## Best Practices

### 🎯 Content Guidelines
1. **Keep descriptions concise** - Aim for 1-2 sentences for projects
2. **Use consistent formatting** - Follow the same pattern for periods and titles
3. **Order matters** - Use the Order field to showcase your best work first
4. **Regular updates** - Keep your content current and relevant

### 🖼️ Image Guidelines
1. **Optimal size:** 800x600 pixels or similar aspect ratio
2. **File size:** Keep under 2MB for faster loading
3. **Format:** JPG or PNG recommended
4. **Content:** Screenshots, mockups, or project logos work best

### 🔗 Link Guidelines
1. **Demo Links:** Should be live, working applications
2. **Code Links:** Usually GitHub repositories
3. **Testing:** Always test your links before saving
4. **HTTPS:** Use secure links when possible

## Quick Actions

### Adding New Content
1. Go to the respective section in admin
2. Click "Add [Education/Experience/Project]"
3. Fill in the required fields
4. Set appropriate Order number
5. Check "Is Active"
6. Save

### Editing Existing Content
1. Go to the respective section in admin
2. Click on the item you want to edit
3. Make your changes
4. Save

### Reordering Items
1. Edit the Order field for each item
2. Lower numbers appear first
3. Save changes

### Hiding Content Temporarily
1. Edit the item
2. Uncheck "Is Active"
3. Save (item won't appear on website but data is preserved)

## Technical Notes

### Database
- All content is stored in SQLite database
- Regular backups recommended for production
- Changes are immediate after saving

### Images
- Uploaded to `media/projects/` folder
- Automatically resized for web display
- Original files are preserved

### Performance
- Images are optimized for web display
- Database queries are optimized
- Caching can be added for production

## Troubleshooting

### Common Issues
1. **Images not showing:** Check file permissions and media settings
2. **Links not working:** Verify URLs include http:// or https://
3. **Order not updating:** Clear browser cache and refresh
4. **Admin access denied:** Check superuser credentials

### Getting Help
- Check Django admin documentation
- Verify all required fields are filled
- Ensure "Is Active" is checked for content to appear

## Security Notes
- Keep admin credentials secure
- Use strong passwords
- Consider two-factor authentication for production
- Regular security updates recommended

---

**Last Updated:** June 2025
**Version:** 1.0
