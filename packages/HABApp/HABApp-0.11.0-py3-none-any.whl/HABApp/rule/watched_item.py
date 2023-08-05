import datetime

from HABApp.core import EventBus, Items
from HABApp.core.events import ValueNoChangeEvent, ValueNoUpdateEvent


class WatchedItem:
    def __init__(self, name, constant_time: int, watch_only_changes=False):
        assert isinstance(name, str)
        assert isinstance(constant_time, int)
        assert isinstance(watch_only_changes, bool)

        self.name: str = name
        self.duration_const = datetime.timedelta(seconds=constant_time)
        self.executed = False

        self.__watch_only_changes = watch_only_changes

        self.is_canceled = False

    def check(self, now):
        if self.is_canceled:
            return None

        try:
            item = Items.get_item(self.name)
        except Items.ItemNotFoundException:
            return None

        timestamp = item._last_change if self.__watch_only_changes else item._last_update
        duration = now - timestamp
        if duration < self.duration_const:
            self.executed = False
            return None

        if self.executed:
            return None

        EventBus.post_event(
            self.name,
            (ValueNoChangeEvent if self.__watch_only_changes else ValueNoUpdateEvent)(
                self.name, item.value, int(duration.total_seconds())
            )
        )
        self.executed = True

    def cancel(self):
        self.is_canceled = True
