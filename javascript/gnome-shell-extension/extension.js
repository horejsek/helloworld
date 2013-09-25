
const St = imports.gi.St;
const Main = imports.ui.main;
const Tweener = imports.ui.tweener;
const Gettext = imports.gettext;
const _ = Gettext.gettext;
const MessageTray = imports.ui.messageTray;

let text, button;

function init() {
    button = new St.Bin({
        style_class: 'panel-button',
        reactive: true,
        can_focus: true,
        x_fill: true,
        y_fill: false,
        track_hover: true
    });
    let icon = new St.Icon({
        icon_name: 'accessories-character-map',
        icon_type: St.IconType.SYMBOLIC,
        style_class: 'system-status-icon'
    });
    button.set_child(icon);
    button.connect('button-press-event', showHelloWorld);
}

function enable() {
    Main.panel._rightBox.insert_child_at_index(button, 0);
}

function disable() {
    Main.panel._rightBox.remove_child(button);
}

function showHelloWorld() {
    let msg = _("Hello, world!");
    showText(msg);
    showNotify(msg);
}

function showText(msg) {
    text = new St.Label({
        style_class: 'helloworld-label',
        text: msg
    });
    Main.uiGroup.add_actor(text);
    text.opacity = 255;
    let monitor = Main.layoutManager.primaryMonitor;
    text.set_position(
        Math.floor(monitor.width / 2 - text.width / 2),
        Math.floor(monitor.height / 2 - text.height / 2)
    );
    Tweener.addTween(text, {
        opacity: 0,
        time: 2,
        transition: 'easeOutQuad',
        onComplete: hideText
    });
}

function hideText() {
    Main.uiGroup.remove_actor(text);
    text = null;
}

function showNotify(msg)
{
    let source = new MessageTray.SystemNotificationSource();
    Main.messageTray.add(source);
    let notification = new MessageTray.Notification(source, msg, null);
    notification.setTransient(true);
    source.notify(notification);
}