
sudo pip install happybase
#python2


import sys
from google.cloud import bigtable
from google.cloud import happybase

client = bigtable.Client(project=project_id, admin=True)
instance = client.instance(instance_id)
connection = happybase.Connection(instance=instance)

print('Creating the {} table.'.format(table_name))
column_family_name = 'cf1'
connection.create_table(
    table_name,
    {
        column_family_name: dict()  # Use default options.
    })

print('Writing some greetings to the table.')
        table = connection.table(table_name)
        column_name = '{fam}:greeting'.format(fam=column_family_name)
        greetings = [
            'Hello World!',
            'Hello Cloud Bigtable!',
            'Hello HappyBase!',
        ]

        for i, value in enumerate(greetings):
            row_key = 'greeting{}'.format(i)
            table.put(row_key, {column_name: value})

        print('Getting a single greeting by row key.')
        key = 'greeting0'.encode('utf-8')
        row = table.row(key)
        print('\t{}: {}'.format(key, row[column_name.encode('utf-8')]))

        print('Scanning for all greetings:')

        for key, row in table.scan():
            print('\t{}: {}'.format(key, row[column_name.encode('utf-8')]))

        print('Deleting the {} table.'.format(table_name))
        connection.delete_table(table_name)

    finally:
        connection.close()


if __name__ == '__main__':
    parser = argparse.ArgumentParser(
        description=__doc__,
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)
    parser.add_argument('project_id', help='Your Cloud Platform project ID.')
    parser.add_argument(
        'instance_id', help='ID of the Cloud Bigtable instance to connect to.')
    parser.add_argument(
        '--table',
        help='Table to create and destroy.',
        default='Hello-Bigtable')

    args = parser.parse_args()
    main(args.project_id, args.instance_id, args.table)


------------------

