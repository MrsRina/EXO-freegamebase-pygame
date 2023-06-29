# EXO-freegamebase pygame
 It's a good game base made in Python and Pygame, have a system event and works great.

# How continue;
- Make a simple fork to continue the work as your own game, use the event manager correct.

```
# System with clients if you want use to do some pygame online game.
# To start continue the game go in GUI > GameGUI and in run() command is able to do what you want.

:)

```

```
event_manager.createEvent("GamePause", "When game pause", False);

event_manager.getEventClazz("GamePause").setAction(True) // Or off.
event_manager.getEventClazz("GamePause").getAction(); // Like getEvent();

if event_manager.getEvent("GamePause"):
 ...

# if you want combine a event pygame with it, just create a event in __init__ in EventManager;
# Or create in other place lol.

```

You can do what you want.
```
Configure.
__init__.py >

# You can able name and things.

```
