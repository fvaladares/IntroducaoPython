
if __name__ == '__main__':

    status_code = 200

    if status_code == 200:
        print('Requisição aceita.')
    elif status_code == 404:
        print('Recurso não encontrado.')
    elif status_code == 500:
        print('Erro no servidor. Por favor, tente novamente mais tarde.')
    else:
        print('Código de erro desconhecido.')

    print('\n----------------------------\n')
    print('Avaliando o status code usando o match: ')
    match status_code:
        case 200:
            print('Requisição aceita.')

        case 404:
            print('Recurso não encontrado.')

        case 500:
            print('Erro no servidor. Por favor, tente novamente mais tarde.')

        case _:
            print('Código de erro desconhecido.')


    day = "Monday"

    # Match the day to predefined patterns
    match day:
        case "Saturday" | "Sunday":
            print(f"{day} is a weekend.")  # Match weekends
        case "Monday" | "Tuesday" | "Wednesday" | "Thursday" | "Friday":
            print(f"{day} is a weekday.")  # Match weekdays
        case _:
            print("That's not a valid day of the week.")  # Default case

# Monday is a weekday.