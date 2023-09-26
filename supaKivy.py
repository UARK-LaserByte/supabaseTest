import kivy
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.gridlayout import GridLayout
from supabase import create_client

# Replace with your Supabase project URL and API key
supabase_url = 'https://zjhemihkjcspikabnabb.supabase.co'
supabase_key = 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6InpqaGVtaWhramNzcGlrYWJuYWJiIiwicm9sZSI6ImFub24iLCJpYXQiOjE2OTQ1NDU4ODUsImV4cCI6MjAxMDEyMTg4NX0.OlzWaElvTMe1eUfFTkxSmG7y9xaKGDWgV5mMjlzDCuU'

supabase = create_client(supabase_url, supabase_key)

class MyApp(App):
    def build(self):
        layout = BoxLayout(orientation='vertical')
        self.table_grid = GridLayout(cols=2)  # Create a grid layout for the table
        layout.add_widget(self.table_grid)

        # Add a button to trigger data retrieval
        fetch_button = Button(text='Fetch Data')
        fetch_button.bind(on_release=self.fetch_data)
        layout.add_widget(fetch_button)

        return layout

    def fetch_data(self, instance):
        # Replace 'your-table-name' with the name of your Supabase table
        table_name = 'player'

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
