import sys
import notify2

from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QSystemTrayIcon, QApplication, QMenu, QAction

from kangry_pomodoro.pomodoro_timer import PomodoroState, Pomodoro


def menu_opening_event(pomodoro: Pomodoro, menu_action: QAction):
    time = int(pomodoro.get_time())
    menu_action.setText('{:0>2}:{:0>2}'.format(time // 60, time % 60))


def state_changed_slot(*args, **kwargs):
    sender: Pomodoro = args[0]
    previous_state, state = kwargs.get('previous_state'), kwargs.get('state')
    if state is PomodoroState.Stopped:
        if previous_state is PomodoroState.WorkTime:
            title = "Пора передохнуть"
            mes = "Сделайте перерыв. Это полезно."
        elif previous_state in [PomodoroState.LongBreak, PomodoroState.ShortBreak]:
            title = "Перервы закончился"
            mes = "Пора приниматься за работу."
        else:
            return

        n = notify2.Notification(title, message=mes)
        n.add_action('Ok', 'Принять', lambda obj, key, data=None: sender.continue_work())
        n.show()


def create_pomodoro_timer(**kwargs):
    obj = Pomodoro()
    obj.work_time = kwargs.get('work_time', 30) * 60
    obj.short_break = kwargs.get('short_break', 5) * 60
    obj.long_break = kwargs.get('long_break', 25) * 60

    obj.state_changed_event.append(state_changed_slot)

    return obj


def launch_app(**kwargs):
    app = QApplication(sys.argv)
    pomodoro = create_pomodoro_timer(**kwargs)

    # Подключаемся к DBus для уведомлений
    notify2.init('Pomodoro', 'glib')

    tray_icon: QSystemTrayIcon = QSystemTrayIcon(QIcon('static/icon.png'), app)
    tray_icon.setToolTip('Manage your time!')
    tray_icon.show()

    menu = QMenu()
    display_menu: QAction = menu.addAction('00:00')
    display_menu.setEnabled(False)
    pause_menu: QAction = menu.addAction('Pause')
    pause_menu.triggered.connect(pomodoro.pause)
    continue_menu: QAction = menu.addAction('Continue')
    continue_menu.triggered.connect(pomodoro.continue_work)
    exit_menu = menu.addAction('Exit')
    exit_menu.triggered.connect(app.quit)

    tray_icon.setContextMenu(menu)
    tray_icon.contextMenu().aboutToShow.connect(lambda: menu_opening_event(pomodoro, display_menu))

    pomodoro.start()

    n = notify2.Notification('Pomodoro запущен')
    n.timeout = 700
    n.show()

    app.exit(app.exec_())
