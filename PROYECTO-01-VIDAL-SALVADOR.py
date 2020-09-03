from lifestore_file import lifestore_products, lifestore_sales, lifestore_searches

#Register admin users.
admin_users = []
while admin_users == []:
    print('\nThere is no admin users registered.')
    username = input('\nPlease register an admin user: ')
    password = input('Please enter the password: ')
    admin_users.append([username, password])
    other_user = input('\nDo you want to register another admin user? (Yes/No) ')
    while other_user == 'Yes':
        username = input('\nPlease enter the username of a admin user: ')
        password = input('Please enter the password: ')
        admin_users.append([username, password])
        other_user = input('\nDo you want to register another admin user? (Yes/No) ')

#Login.
valid_username = input('\nPlease enter an admin username: ')
valid_password = input('Please enter the password: ')
admin = 0

for user in admin_users:
    if user[0] == valid_username and user[1] == valid_password:
        print('\nWelcome to Life Store', valid_username)
        admin = 1
        break
    else:
        continue

if admin == 1:
    leave = False

    while not leave:
        #General menu.
        options = int(input(
        '\n**************MENU**************: ',
        '\n(1)Top-selling products.',
        '\n(2)Products with the highest searches.'
        '\n(3)Products with minors sales by category.',
        '\n(4)Products with fewer searches by category.'
        '\n(5)Products with the best reviews.',
        '\n(6)Products with the worst reviews.',
        '\n(7)Finance.'
        '\n(8)Leave.',
        '\nSelect an option: '))

        if options == 1:
            #Top-selling products.
            counter = 0
            selling_list = []

            for product in lifestore_products:
                for sale in lifestore_sales:
                    if product[0] == sale[1]:
                        counter += 1
                if counter != 0:
                    selling_list.append([product[1], counter])
                counter = 0

            #Sort the list from highest to lowest.
            length = len(selling_list)

            for i in range(0, length): 
                for j in range(0, length-i-1): 
                    if (selling_list[j][1] < selling_list[j + 1][1]): 
                        tempo = selling_list[j] 
                        selling_list[j]= selling_list[j + 1] 
                        selling_list[j + 1]= tempo

            #Show the top-selling products.
            print('\n\nTop-selling products are:\n')
            product_index = 1
            for k in range(len(selling_list)):
                print(product_index, '-', selling_list[k][0])
                product_index += 1
 
        elif options == 2:
            #Top-searches products.
            counter = 0
            searches_list = []

            for product in lifestore_products:
                for search in lifestore_searches:
                    if product[0] == search[1]:
                        counter += 1
                if counter != 0:
                    searches_list.append([product[1], counter])
                counter = 0

            #Sort the list from highest to lowest.
            length = len(searches_list)

            for i in range(0, length): 
                for j in range(0, length-i-1): 
                    if (searches_list[j][1] < searches_list[j + 1][1]): 
                        tempo = searches_list[j] 
                        searches_list[j]= searches_list[j + 1] 
                        searches_list[j + 1]= tempo

            #Show the top-selling products.
            print('\n\nTop-searches products are:\n')
            product_index = 1
            for k in range(len(searches_list)):
                print(product_index, '-', searches_list[k][0])
                product_index += 1
        
        elif options == 3:
            #Products with minors sales by category.
            leave_category_menu = False

            while not leave_category_menu:
                #Category Menu.
                print('\n**************Categories**************: ')
                counter = 0
                category_list = []
                no_repeating_categories = []

                for product in lifestore_products:
                    category_list.append(product[3])
                    for category in category_list:
                        if category not in no_repeating_categories:
                            no_repeating_categories.append(category)
                category_index = 1
                for category in no_repeating_categories:
                    print('(', category_index, ')', '-', category)
                    category_index += 1
                print('( 0 )- Leave')
                selected_category = int(input('Select an option: '))

                #Leave category menu.
                if selected_category == 0:
                    leave_category_menu = True
                    continue
                
                if selected_category != 0 and selected_category != 1 and selected_category != 2 and selected_category != 3 and selected_category != 4 and selected_category != 5 and selected_category != 6 and selected_category != 7 and selected_category != 8:
                    print('\n\nThat is not an option. Please choose a valid option.')
                    continue

                #Create a list of products by category.
                single_category_list = []
                for product in lifestore_products:
                    if no_repeating_categories[selected_category-1] == product[3]:
                        single_category_list.append(product)

                #Minor sales products.
                counter = 0
                selling_list = []

                for product in single_category_list:
                    for sale in lifestore_sales:
                        if product[0] == sale[1]:
                            counter += 1
                    selling_list.append([product[1], counter])
                    counter = 0

                #Sort the list from lowest to highest.
                length = len(selling_list)

                for i in range(0, length): 
                    for j in range(0, length-i-1): 
                        if (selling_list[j][1] > selling_list[j + 1][1]): 
                            tempo = selling_list[j] 
                            selling_list[j]= selling_list[j + 1] 
                            selling_list[j + 1]= tempo

                #Show the top-selling products.
                print('\n\nMinor sales products of that category are:\n')
                product_index = 1
                for k in range(len(selling_list)):
                    print(product_index, '-', selling_list[k][0])
                    product_index += 1

        elif options == 4:
            leave_category_menu = False

            while not leave_category_menu:
                #Category Menu.
                print('\n**************Categories**************: ')
                counter = 0
                category_list = []
                no_repeating_categories = []

                for product in lifestore_products:
                    category_list.append(product[3])
                    for category in category_list:
                        if category not in no_repeating_categories:
                            no_repeating_categories.append(category)
                category_index = 1
                for category in no_repeating_categories:
                    print('(', category_index, ')', '-', category)
                    category_index += 1
                print('( 0 )- Leave')
                selected_category = int(input('Select an option: '))

                #Leave category menu.
                if selected_category == 0:
                    leave_category_menu = True
                    continue
                
                if selected_category != 0 and selected_category != 1 and selected_category != 2 and selected_category != 3 and selected_category != 4 and selected_category != 5 and selected_category != 6 and selected_category != 7 and selected_category != 8:
                    print('\n\nThat is not an option. Please choose a valid option.')
                    continue

                #Create a list of products by category.
                single_category_list = []
                for product in lifestore_products:
                    if no_repeating_categories[selected_category-1] == product[3]:
                        single_category_list.append(product)

                #Minor sales products.
                counter = 0
                searches_list = []

                for product in single_category_list:
                    for search in lifestore_searches:
                        if product[0] == search[1]:
                            counter += 1
                    searches_list.append([product[1], counter])
                    counter = 0

                #Sort the list from lowest to highest.
                length = len(searches_list)

                for i in range(0, length): 
                    for j in range(0, length-i-1): 
                        if (searches_list[j][1] > searches_list[j + 1][1]): 
                            tempo = searches_list[j] 
                            searches_list[j]= searches_list[j + 1] 
                            searches_list[j + 1]= tempo

                #Show the top-searches products.
                print('\n\nThe products with the fewer searches of that category are:\n')
                product_index = 1
                for k in range(len(searches_list)):
                    print(product_index, '-', searches_list[k][0])
                    product_index += 1

        elif options == 5:
            #Create a list of average scores for each product.
            sum_score = 0
            average = 0
            counter = 0
            average_score = []
            for product in lifestore_products:
                for sale in lifestore_sales:
                    if product[0] == sale[1]:
                        sum_score += sale[2]
                        counter += 1
                    if counter != 0:
                        average = sum_score / counter
                average_score.append([average, product[1]])
                sum_score = 0
                average = 0
                counter = 0

            #Sort the list.
            length = len(average_score)

            for i in range(0, length): 
                for j in range(0, length-i-1): 
                    if (average_score[j][0] < average_score[j + 1][0]): 
                        tempo = average_score[j] 
                        average_score[j] = average_score[j + 1] 
                        average_score[j + 1]= tempo

            #Show the list of the best products based on reviews.
            counter = 1
            print('\n\nThe best products based on reviews: \n')
            for element in range(0, 20):
                print(counter, '-', average_score[element][1])
                counter += 1

        elif options == 6:
            #Create a list of average scores for each product.
            sum_score = 0
            average = 0
            counter = 0
            average_score = []
            for product in lifestore_products:
                for sale in lifestore_sales:
                    if product[0] == sale[1]:
                        sum_score += sale[2]
                        counter += 1
                    if counter != 0:
                        average = sum_score / counter
                average_score.append([average, product[1]])
                sum_score = 0
                average = 0
                counter = 0       

            #Sort the list of average scores for each product.
            length = len(average_score)

            for i in range(0, length): 
                for j in range(0, length-i-1): 
                    if (average_score[j][0] > average_score[j + 1][0]): 
                        tempo = average_score[j] 
                        average_score[j] = average_score[j + 1] 
                        average_score[j + 1]= tempo

            #Show the list of the best products based on reviews.
            counter = 1
            print('\n\nThe worst products based on reviews: \n')
            for element in range(0, 20):
                print(counter, '-', average_score[element][1])
                counter += 1

        elif options == 7:
            #Create a revenue list.
            counter = 0
            revenue_list = []

            for product in lifestore_products:
                for sale in lifestore_sales:
                    if product[0] == sale[1]:
                        counter += 1
                        if counter != 0:
                            revenue_list.append(product[2])
                counter = 0

            #Sum all the values on the list.
            total_revenue = 0
            for value in revenue_list:
                total_revenue += value
            print('\n\nThe total revenue is:', total_revenue)
            
            monthly_revenue = []
            #Create a list [sale, month].
            for product in lifestore_products:
                for sale in lifestore_sales:
                    if product[0] == sale[1]:
                        counter += 1
                        if counter != 0:
                            month = int(sale[3][3:5])
                            monthly_revenue.append([product[2], month])
                counter = 0

            #Sort the list.
            month_total_revenue = 0
            sort_month_revenue = []
            for value in range(1, 13):
                for element in monthly_revenue:
                    if element[1] == value:
                        sort_month_revenue.append(element)

            #Create a list of average revenue for each month.
            sum_month_revenue = 0
            average = 0
            counter = 0
            monthly_average_revenue = []
            monthly_sales_revenue = []
            for value in range(1, 13):
                for item in sort_month_revenue:
                    if item[1] == value:
                        sum_month_revenue += item[0]
                        counter +=1
                    if counter != 0:
                        average = sum_month_revenue / counter
                monthly_average_revenue.append([round(average, 2)])
                monthly_sales_revenue.append([sum_month_revenue, value])
                sum_month_revenue = 0
                average = 0
                counter = 0

            #Show the average revenue for each month.
            counter = 0
            print('\n\n***The average revenue for each month was: ***')
            for revenue in monthly_average_revenue:
                counter += 1
                if counter == 1:
                    print('The average revenue on January was', revenue[0])
                elif counter == 2:
                    print('The average revenue on February was', revenue[0])
                elif counter == 3:
                    print('The average revenue on March was', revenue[0])
                elif counter == 4:
                    print('The average revenue on April was', revenue[0])
                elif counter == 5:
                    print('The average revenue on May was', revenue[0])
                elif counter == 6:
                    print('The average revenue on June was', revenue[0])
                elif counter == 7:
                    print('The average revenue on July was', revenue[0])
                elif counter == 8:
                    print('The average revenue on August was', revenue[0])
                elif counter == 9:
                    print('The average revenue on September was', revenue[0])
                elif counter == 10:
                    print('The average revenue on October was', revenue[0])
                elif counter == 11:
                    print('The average revenue on November was', revenue[0])
                elif counter == 12:
                    print('The average revenue on December was', revenue[0])

            #Show the annual revenue.
            print('\n\nThe annual revenue is:', total_revenue)

            #Sort list of monthly sales.
            length = len(monthly_sales_revenue)

            for i in range(0, length): 
                for j in range(0, length-i-1): 
                    if (monthly_sales_revenue[j][0] < monthly_sales_revenue[j + 1][0]): 
                        tempo = monthly_sales_revenue[j] 
                        monthly_sales_revenue[j] = monthly_sales_revenue[j + 1] 
                        monthly_sales_revenue[j + 1]= tempo

            #Show months with more sales.
            print('\n\n***The months with more sales are: ***')
            for revenue in monthly_sales_revenue:
                if revenue[1] == 1:
                    print('The monthly sale on January was', revenue[0])
                elif revenue[1] == 2:
                    print('The monthly sale on February was', revenue[0])
                elif revenue[1] == 3:
                    print('The monthly sale on March was', revenue[0])
                elif revenue[1] == 4:
                    print('The monthly sale on April was', revenue[0])
                elif revenue[1] == 5:
                    print('The monthly sale on May was', revenue[0])
                elif revenue[1] == 6:
                    print('The monthly sale on June was', revenue[0])
                elif revenue[1] == 7:
                    print('The monthly sale on July was', revenue[0])
                elif revenue[1] == 8:
                    print('The monthly sale on August was', revenue[0])
                elif revenue[1] == 9:
                    print('The monthly sale on September was', revenue[0])
                elif revenue[1] == 10:
                    print('The monthly sale on October was', revenue[0])
                elif revenue[1] == 11:
                    print('The monthly sale on November was', revenue[0])
                elif revenue[1] == 12:
                    print('The monthly sale on December was', revenue[0])
         
        elif options == 8:
            #Change the value of leave to break the while and end the script.
            leave = True
        
        else:
        #Message show in case of enter a value out of the menu.
            print('\n\nThat is not an option. Please choose a valid option.')

#Message show in case of enter a value out of the menu.
else:
    print('\n\nSorry, you are not an admin')
