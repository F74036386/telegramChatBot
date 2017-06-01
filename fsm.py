from transitions.extensions import GraphMachine


class TocMachine(GraphMachine):
    def __init__(self, **machine_configs):
        self.machine = GraphMachine(
            model = self,
            **machine_configs
        )

    def is_going_to_92(self, update):
        text = update.message.text
        return text.lower() == '92'

    def is_going_to_95(self, update):
        text = update.message.text
        return text.lower() == '95'
    
    def is_going_to_98(self, update):
        text = update.message.text
        return text.lower() == '98'

    def is_going_to_amo(self, update):
        text = update.message.text
        return text.lower() == 'amount'

    def is_going_to_full(self, update):
        text = update.message.text
        return text.lower() == 'full'

    def is_going_to_cash(self, update):
        text = update.message.text
        return text.lower() == 'cash'
    
    def is_going_to_credit(self, update):
        text = update.message.text
        return text.lower() == 'credit card'

    def on_enter_92(self, update):
        update.message.reply_text("you need to 92")
        update.message.reply_text("full or amount of oil")
    def on_enter_95(self, update):
        update.message.reply_text("you need to 95")   
        update.message.reply_text("full or amount of oil")
    def on_enter_98(self, update):
        update.message.reply_text("you need to 98")
        update.message.reply_text("full or amount of oil")
    
    def on_enter_full(self, update):
        update.message.reply_text("you need to make it full")
        update.message.reply_text("pay by cash or credit card")
    
    def on_enter_amo(self, update):
        update.message.reply_text("you need to get some oil")
        update.message.reply_text("pay by cash or credit")
    	
    def on_enter_cash(self, update):
        update.message.reply_text("you need to pay by cash")
        update.message.reply_text("thanks")
        self.go_back(update)
    
    def on_enter_credit(self, update):
        update.message.reply_text("you needto pay by credit card")
        update.message.reply_text("thanks")
        self.go_back(update)

#    def on_exit_state1(self, update):
#        print('Leaving state1')

#    def on_enter_state2(self, update):
#        update.message.reply_text("I'm entering state2")
#        self.go_back(update)

#    def on_exit_state2(self, update):
#        print('Leaving state2')
