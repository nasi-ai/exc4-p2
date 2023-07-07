from abc import ABC, abstractmethod


class Participant(ABC):
    def __init__(self, national_id, name, lastname, academic_major, address):
        self.__national_id = national_id
        self.__name = name
        self.__lastname = lastname
        self.__academic_major = academic_major
        self.__address = address
        self._final_score = None

    # Getter methods
    @property
    def national_id(self):
        return self.__national_id

    @property
    def name(self):
        return self.__name

    @property
    def lastname(self):
        return self.__lastname

    @property
    def address(self):
        return self.__address

    @property
    def major(self):
        return self.__academic_major

    # Setter Methods
    @name.setter
    def name(self, name: str):
        # Check if name is str
        if isinstance(name, str):
            self.__name = name
        else:
            raise ValueError('Send a string to set name')

    @lastname.setter
    def lastname(self, lastname: str):
        # Check if name is str
        if isinstance(lastname, str):
            self.__lastname = lastname
        else:
            print('Send a string to set lastname')

    @address.setter
    def address(self, address: str):
        # Check if name is str
        if isinstance(address, str):
            self.__address = address
        else:
            print('Send a string to set address')

    @major.setter
    def major(self, major):
        self.__academic_major = major

    # Required method
    @abstractmethod
    def calculate_grade(self):
        pass

    def __str__(self):
        return f'id : {self.national_id}\n' \
               f'name: {self.name}\n' \
               f'lastname: {self.lastname}\n' \
               f'Major: {self.major}\n' \
               f'Address: {self.address}\n' \
               f'final grade: {self.calculate_grade()}'


class Azad(Participant):
    def __init__(self, national_id: float, name, lastname, academic_major, address,
                 interview_score, employ_test_score):
        super().__init__(national_id, name, lastname, academic_major, address)
        self._interview_score = interview_score
        self._employ_test_score = employ_test_score

    def calculate_grade(self):
        # Ensure both scores are between 0 and 100
        if not (0 <= self._interview_score <= 100 and 0 <= self._employ_test_score <= 100):
            raise ValueError('Invalid interview score or employee test score! They must be between 0 and 100')

        final_score = (self._interview_score + self._employ_test_score) / 2

        if not (0 <= final_score <= 100):
            raise ValueError('Invalid final score calculation! final score must be between 0, 100')

        return final_score


#  Should write better in the next time ( as an expert )
class Expert(Participant):

    def __init__(self, national_id, name, lastname, academic_major, address, university_rank, average):
        super().__init__(national_id, name, lastname, academic_major, address)

        if university_rank not in (1, 2, 3):
            raise ValueError('University rank should be 1, 2, or 3')

        if university_rank == 1:
            self._uni_rank_grade = 100
        elif university_rank == 2:
            self._uni_rank_grade = 80
        else:
            self._uni_rank_grade = 60

        if average < 16:
            raise ValueError('Your average is not acceptable! It must be 16 or higher')

        if 16 <= average < 17.5:
            self._avg_score = 60
        elif 17.5 <= average < 18.5:
            self._avg_score = 80
        else:
            self._avg_score = 100

    def calculate_grade(self):
        final_grade = (self._avg_score + self._uni_rank_grade) / 2

        if not (0 <= final_grade <= 100):
            raise ValueError('Wrong Calculation!')

        return final_grade


class Employee(Participant):

    def __init__(self, national_id, name, lastname, academic_major, address, avg_performance_score, experience_years):
        super().__init__(national_id, name, lastname, academic_major, address)

        if not (experience_years > 1):
            raise ValueError('Your experience is not sufficient!')

        self._experience_coef = None
        if 1 <= experience_years <= 5:
            self._experience_coef = 0.1
        elif experience_years > 5:
            self._experience_coef = 0.2

        if not (0 <= avg_performance_score <= 100):
            raise ValueError('Invalid avg_performance_score! It should be between 0 and 100.')

        self._avg_performance_score = avg_performance_score

    def calculate_grade(self):

        # Calculate Experience coefficient
        final_grade = self._avg_performance_score + (self._experience_coef * self._avg_performance_score)

        if not (0 <= final_grade <= 120):
            raise ValueError('Calculation Error! final_grade must be between 0 and 120')

        return final_grade


participant1 = Azad(national_id='hgh', name='nastaran', lastname='aki', academic_major='math',
                    address='Msh', interview_score=60, employ_test_score=70)
print(participant1)

participant2 = Expert(national_id='956251', name='ali', lastname='zamani', academic_major='science',
                      address='Msh', university_rank=1, average=17)

participant3 = Employee(national_id='956251', name='ali', lastname='zamani', academic_major='science',
                        address='Msh', experience_years=20, avg_performance_score=90)

# Add Accepted Participants ( grad >= 90) to the list
accepted_participant_list = []
for i in range(1, 4):
    participant_name = 'participant' + str(i)
    participant_name = eval(participant_name)
    if participant_name.calculate_grade() >= 90:
        accepted_participant_list.append(participant_name)

# Show accepted Participants
print('Accepted Participants:\n', '-' * 30)
for p in accepted_participant_list:
    print(p)
    print('-' * 30)
