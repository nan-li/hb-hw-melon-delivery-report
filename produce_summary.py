def print_produce_summary(day, file):
    """
    Prints the day and summary of sales for that day 
    from a log file 
    """

    print(day)
    the_file = open(file)
    for line in the_file:
        line = line.rstrip()
        words = line.split('|')

        melon = words[0]
        count = words[1]
        amount = words[2]

        print("Delivered {} {}s for total of ${}".format(
            count, melon, amount))
    the_file.close()

print_produce_summary("Day 1", "um-deliveries-20140519.txt")
print_produce_summary("Day 2", "um-deliveries-20140520.txt")
print_produce_summary("Day 3", "um-deliveries-20140521.txt")
