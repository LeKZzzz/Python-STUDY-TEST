#include "checktickets.h"
#include "ui_checktickets.h"

CheckTickets::CheckTickets(QWidget *parent) :
    QMainWindow(parent),
    ui(new Ui::CheckTickets)
{
    ui->setupUi(this);
}

CheckTickets::~CheckTickets()
{
    delete ui;
}
