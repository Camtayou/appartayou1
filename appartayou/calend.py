import pycalendar

c = pycalendar.Calendar()

# Affichez les jours d'un mois donné
for day in c.itermonthdays(2020, 1):
    print(day)

# Affichez les événements d'un mois donné
for event in c.itermonthdates(2020, 1):
    print(event)

# Ajoutez un événement au calendrier
c.add_event('Anniversaire de Marie')

# Supprimez un événement du calendrier
c.remove_event('Anniversaire de Marie')


# Affichez un événement au format ISO
print(c.format_event_iso('Anniversaire de Marie'))

# Affichez un événement au format ISO date
print(c.format_event_date_iso('Anniversaire de Marie'))

# Affichez un événement au format ISO heure
print(c.format_event_time_iso('Anniversaire de Marie'))
