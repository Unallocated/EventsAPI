import authenticate

class UASCalendar:
    __calendar_id = "primary"
    __service = authenticate.authenticate()
    
    def create_event(self, event_body, notify=False):
        event = self.__service.events().insert(calendarId=self.__calendar_id, body=event_body).execute()
        return event['id']

    def delete_event(event_id, notify=False):
        self.__service.events().delete(calendarId=self.__calendar_id, eventId=event_id, sendNotifications=notify)

    def delete_events(event_id_list, notify=False):
        for eventt_id in event_id_list:
            self.__service.events().delete(calendarId=self.__calendar_id, eventId=event_id, sendNotifications=notify)

    def update_event(self, event_id, event_body, notify=False):
        return self.__service.events().update(calendarId=self.__calendar_id, eventId=event_id, body=event_body, sendNotifications=notify).execute()
