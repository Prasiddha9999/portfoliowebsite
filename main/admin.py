from django.contrib import admin
from .models import Contact, Education, Experience, Project, About, DailyHoroscope

@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'subject', 'created_at')
    list_filter = ('created_at',)
    search_fields = ('name', 'email', 'subject', 'message')
    readonly_fields = ('created_at',)
    date_hierarchy = 'created_at'
    ordering = ('-created_at',)


@admin.register(Education)
class EducationAdmin(admin.ModelAdmin):
    list_display = ('degree', 'institution', 'period', 'order', 'is_active', 'created_at')
    list_filter = ('is_active', 'created_at')
    search_fields = ('degree', 'institution', 'description')
    list_editable = ('order', 'is_active')
    readonly_fields = ('created_at', 'updated_at')
    ordering = ('order', '-created_at')

    fieldsets = (
        ('Basic Information', {
            'fields': ('degree', 'institution', 'period', 'description')
        }),
        ('Display Settings', {
            'fields': ('order', 'is_active')
        }),
        ('Timestamps', {
            'fields': ('created_at', 'updated_at'),
            'classes': ('collapse',)
        }),
    )


@admin.register(Experience)
class ExperienceAdmin(admin.ModelAdmin):
    list_display = ('title', 'company', 'period', 'order', 'is_active', 'created_at')
    list_filter = ('is_active', 'created_at')
    search_fields = ('title', 'company', 'responsibilities')
    list_editable = ('order', 'is_active')
    readonly_fields = ('created_at', 'updated_at')
    ordering = ('order', '-created_at')

    fieldsets = (
        ('Basic Information', {
            'fields': ('title', 'company', 'period')
        }),
        ('Job Details', {
            'fields': ('responsibilities',),
            'description': 'Enter each responsibility on a new line'
        }),
        ('Display Settings', {
            'fields': ('order', 'is_active')
        }),
        ('Timestamps', {
            'fields': ('created_at', 'updated_at'),
            'classes': ('collapse',)
        }),
    )


@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ('title', 'category', 'order', 'is_featured', 'is_active', 'created_at')
    list_filter = ('is_featured', 'is_active', 'category', 'created_at')
    search_fields = ('title', 'description', 'technologies')
    list_editable = ('order', 'is_featured', 'is_active')
    readonly_fields = ('created_at', 'updated_at')
    ordering = ('order', '-created_at')

    fieldsets = (
        ('Basic Information', {
            'fields': ('title', 'description', 'category')
        }),
        ('Media & Links', {
            'fields': ('image', 'demo_link', 'code_link')
        }),
        ('Technical Details', {
            'fields': ('technologies',),
            'description': 'Enter technologies separated by commas (e.g., Python, Django, JavaScript)'
        }),
        ('Display Settings', {
            'fields': ('order', 'is_featured', 'is_active')
        }),
        ('Timestamps', {
            'fields': ('created_at', 'updated_at'),
            'classes': ('collapse',)
        }),
    )

    def save_model(self, request, obj, form, change):
        """Custom save to handle image uploads"""
        super().save_model(request, obj, form, change)


@admin.register(About)
class AboutAdmin(admin.ModelAdmin):
    list_display = ('title', 'is_active', 'created_at', 'updated_at')
    list_filter = ('is_active', 'created_at')
    search_fields = ('title', 'description')
    list_editable = ('is_active',)
    readonly_fields = ('created_at', 'updated_at')

    fieldsets = (
        ('Content', {
            'fields': ('title', 'description')
        }),
        ('Media', {
            'fields': ('photo',)
        }),
        ('Settings', {
            'fields': ('is_active',)
        }),
        ('Timestamps', {
            'fields': ('created_at', 'updated_at'),
            'classes': ('collapse',)
        }),
    )

    def has_add_permission(self, request):
        """Limit to one About instance, but allow if none exists"""
        if About.objects.exists():
            return False
        return super().has_add_permission(request)

    def has_delete_permission(self, request, obj=None):
        """Prevent deletion if it's the only About instance"""
        if About.objects.count() <= 1:
            return False
        return super().has_delete_permission(request, obj)


@admin.register(DailyHoroscope)
class DailyHoroscopeAdmin(admin.ModelAdmin):
    list_display = ('zodiac_sign', 'date', 'mood', 'lucky_number', 'lucky_color', 'is_active', 'updated_at')
    list_filter = ('zodiac_sign', 'date', 'mood', 'is_active', 'created_at')
    search_fields = ('zodiac_sign', 'description', 'lucky_color', 'compatibility')
    list_editable = ('is_active',)
    readonly_fields = ('created_at', 'updated_at')
    ordering = ('-date', 'zodiac_sign')
    date_hierarchy = 'date'

    fieldsets = (
        ('Basic Information', {
            'fields': ('zodiac_sign', 'date', 'is_active')
        }),
        ('Horoscope Content', {
            'fields': ('description',),
            'description': 'Write the main horoscope prediction for this zodiac sign'
        }),
        ('Lucky Information', {
            'fields': ('lucky_number', 'lucky_color', 'lucky_time', 'mood'),
            'description': 'Set lucky numbers, colors, and other positive attributes'
        }),
        ('Compatibility', {
            'fields': ('compatibility',),
            'description': 'Optional: Best compatibility zodiac sign for today'
        }),
        ('Timestamps', {
            'fields': ('created_at', 'updated_at'),
            'classes': ('collapse',)
        }),
    )

    def get_queryset(self, request):
        """Show most recent horoscopes first"""
        return super().get_queryset(request).select_related()

    def save_model(self, request, obj, form, change):
        """Custom save with validation"""
        super().save_model(request, obj, form, change)

    actions = ['duplicate_for_today', 'mark_active', 'mark_inactive']

    def duplicate_for_today(self, request, queryset):
        """Duplicate selected horoscopes for today's date"""
        from django.utils import timezone
        today = timezone.now().date()

        duplicated = 0
        for horoscope in queryset:
            # Check if horoscope for this sign already exists for today
            if not DailyHoroscope.objects.filter(zodiac_sign=horoscope.zodiac_sign, date=today).exists():
                DailyHoroscope.objects.create(
                    zodiac_sign=horoscope.zodiac_sign,
                    date=today,
                    description=horoscope.description,
                    lucky_number=horoscope.lucky_number,
                    lucky_color=horoscope.lucky_color,
                    lucky_time=horoscope.lucky_time,
                    mood=horoscope.mood,
                    compatibility=horoscope.compatibility,
                    is_active=True
                )
                duplicated += 1

        self.message_user(request, f'Successfully duplicated {duplicated} horoscopes for today.')
    duplicate_for_today.short_description = "Duplicate selected horoscopes for today"

    def mark_active(self, request, queryset):
        """Mark selected horoscopes as active"""
        updated = queryset.update(is_active=True)
        self.message_user(request, f'{updated} horoscopes marked as active.')
    mark_active.short_description = "Mark selected horoscopes as active"

    def mark_inactive(self, request, queryset):
        """Mark selected horoscopes as inactive"""
        updated = queryset.update(is_active=False)
        self.message_user(request, f'{updated} horoscopes marked as inactive.')
    mark_inactive.short_description = "Mark selected horoscopes as inactive"
