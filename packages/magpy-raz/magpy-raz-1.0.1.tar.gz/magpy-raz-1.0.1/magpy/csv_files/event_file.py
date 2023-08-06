import magpy.csv_files.base as mc


class EventFile(mc.CsvFile):
    '''
    '''

    __NAME = 'events.csv'
    __HEADER = ('מוקד',
                'פרויקט',
                'תאריך',
                'זמן',
                'חניך',
                'ספרינט',
                'שבוע',
                'ספרינט-שבוע',
                'סוג פעולה',
                'נושא',
                'פעולה')

    def __init__(self, prefix, events):
        super().__init__(file_prefix=prefix,
                         file_name=EventFile.__NAME,
                         header=EventFile.__HEADER,
                         row=lambda event: (event.hub_name,
                                            event.project_name,
                                            event.date,
                                            event.time,
                                            event.student_name,
                                            event.sprint_number,
                                            event.week,
                                            event.sprint_week,
                                            event.action_name,
                                            event.target_type,
                                            event.action_details),
                         data_list=events)
