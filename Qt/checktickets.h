#ifndef CHECKTICKETS_H
#define CHECKTICKETS_H

#include <QMainWindow>

namespace Ui {
class CheckTickets;
}

class CheckTickets : public QMainWindow
{
    Q_OBJECT

public:
    explicit CheckTickets(QWidget *parent = nullptr);
    ~CheckTickets();

private:
    Ui::CheckTickets *ui;
};

#endif // CHECKTICKETS_H
