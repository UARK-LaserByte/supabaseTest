import kivy
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from supabase import create_client

# Replace with your Supabase project URL and API key
supabase_url = 'https://zjhemihkjcspikabnabb.supabase.co'
supabase_key = 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6InpqaGVtaWhramNzcGlrYWJuYWJiIiwicm9sZSI6ImFub24iLCJpYXQiOjE2OTQ1NDU4ODUsImV4cCI6MjAxMDEyMTg4NX0.OlzWaElvTMe1eUfFTkxSmG7y9xaKGDWgV5mMjlzDCuU'

supabase = create_client(supabase_url, supabase_key)

class MyApp(App):
    def build(self):
        layout = BoxLayout(orientation='vertical')
        populate_button = Button(text='Populate Table')
        populate_button.bind(on_release=self.populate_table)
        layout.add_widget(populate_button)
        return layout

    def populate_table(self, instance):
        # Replace 'your-table-name' with the name of your Supabase table
        table_name = 'player'

        # Replace with the data you want to insert into the table
        data_to_insert = [
            {"column1": "value1", "column2": "value2"},
            {"column1": "value3", "column2": "value4"},
            # Add more data rows as needed
        ]

        # Insert data into the table
        response, error = supabase.table(table_name).upsert(data_to_insert, returning="minimal")

        if error:
            print(f"Error: {error}")
        else:
            print("Data inserted successfully")

      def fetch_data(self, instance):
        # Replace 'your-table-name' with the name of your Supabase table
        table_name = 'your-table-name'

        # Fetch data from the Supabase table
        response, error = supabase.table(table_name).select().execute()

        if error:
            print(f"Error: {error}")
        else:
            self.display_data(response)

      def display_data(self, data):
        # Clear the existing table data
        self.table_grid.clear_widgets()

        # Add headers to the table
        headers = data[0].keys()
        for header in headers:
            self.table_grid.add_widget(Label(text=header))

        # Add data rows to the table
        for row in data:
            for header in headers:
                self.table_grid.add_widget(Label(text=str(row[header])))

if __name__ == '__main__':
    MyApp().run()
