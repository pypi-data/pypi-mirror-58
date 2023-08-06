# Mars Utilities

Utilties for building better robot code


View the docs online at [Read the Docs](https://mars-utils.readthedocs.io/en/latest/)

## ControlManager

`ControlManager` provides a wrapper that makes making alternate control modes (alternate drivers, different controlers) incredibly simple. It is designed primarially for MagicRobot components, however, it should work with any type.

See `example/` for an example robot.

### Usage

First, all of the controls must be implemented as classes that subclass `marsutils.ControlInterface`. The primary control code defined in the `teleopPeriodic` method.
Then, you must define the `_DISPLAY_NAME` field which will be displayed on the dashboard autochooser.
You can set `_SORT` to prioritize certain interfaces, the higher the number, the higher on the chooser list.

Because it is a magic bot component, you can access injected components.

But you must make an empty `execute` function to be a valid magicbot function.

After you have the control components there are two ways to create the manager.

### MagicBot magic

If you are using the MagicRobot framework you can use the `@with_ctrl_manager` decorator to automagically set everything up. Just annotate your robot class with `@with_ctrl_manager` and you are done. It will magically detect any `ControlInterfaces`, construct the `ControlManager` and automatically call the periodic functions.

Using the decorator also means you don't need to define an `execute` function.

### Manually

Otherwize, you must must set up manager by initializing `ControlManager` with all of your components _after_ `createObjects` has been called. This is [not technically possible with the MagicBot framework](https://github.com/robotpy/robotpy-wpilib-utilities/issues/21) _yet_.

```python
self.control_manager = marsutils.ControlManager(self.xbox_ctrl, self.joystick_ctrl)
```

After you have created the control manager, you must call its periodic functions. This means adding `self.control_manager.teleopPeriodic()` to your `teleopPeriodic` function and so on for each function you use.
