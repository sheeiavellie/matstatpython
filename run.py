import scripts
import load_data as ds
import utilities as u

def run():    

    sample = ds.load_sample_csv('amogus.csv')

    menu_options = {
    1: 'Moment method',
    2: 'Maximum likelihood estimation',
    3: 'Confidence interval',
    4: 'Exit',
    }

    def print_menu():
        u.clear()
        for key in menu_options.keys():
            print (key, '--', menu_options[key] )

    def option1():
        u.clear()
        print(scripts.get_lambda_mom(sample=sample))
        input()

    def option2():
        u.clear()
        print(scripts.get_lambda_mle(sample=sample))
        input()

    def option3():
        u.clear()
        print(scripts.get_confidence_interval(sample=sample))
        input()
   
    while(True):
        print_menu()
        option = ''
        try:
            option = int(input('Enter your choice: '))
        except:
            print('Wrong input. Please enter a number ...')
            input()
        
        if option == 1:
            option1()
        elif option == 2:
            option2()
        elif option == 3:
            option3()
        elif option == 4:
            u.clear()
            print('Thanks for using my program! https://github.com/sheeiavellie')
            exit()
        else:
            print('Invalid option. Please enter a number between 1 and 4.')    

if __name__ == '__main__':
    run()
