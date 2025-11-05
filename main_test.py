import pandas as pd
from main import filterData


class TestFilterData:
    def getBaseData(self):
        return pd.DataFrame({
            'Age': [25, 29, 30, 35, 18, 65]
        })

    def test_young_age_category(self):
        """Тест категории молодой"""
        # Arrange
        data = self.getBaseData()
        expected_ages = [25, 29, 18]

        # Act
        result = filterData(data, 'Молодой')

        # Assert
        assert len(result) == 3
        assert list(result['Age']) == expected_ages

    def test_middle_age_category(self):
        """Тест категории среднего возраста"""
        # Arrange
        data = self.getBaseData()
        expected_ages = [30, 35]

        # Act
        result = filterData(data, 'Среднего возраста')

        # Assert
        assert len(result) == 2
        assert list(result['Age']) == expected_ages

    def test_elderly_age_category(self):
        """Тест категории пожилых"""
        # Arrange
        data = self.getBaseData()
        expected_ages = [65]

        # Act
        result = filterData(data, 'Пожилой')

        # Assert
        assert len(result) == 1
        assert list(result['Age']) == expected_ages

    def test_empty_result_for_category(self):
        """Тест нет подходящих данных"""
        # Arrange
        data = pd.DataFrame({
            'Age': [15, 18, 29, 79, 91]
        })

        # Act
        result = filterData(data, 'Среднего возраста')

        # Assert
        assert len(result) == 0
        assert result.empty

    def test_elderly_age_for_unexistent_category(self):
        """Тест несуществующая категория"""
        # Arrange
        data = self.getBaseData()
        expected_ages = [65]

        # Act
        result = filterData(data, 'мяу-мяу, мяу-мяу.')

        # Assert
        assert len(result) == 1
        assert list(result['Age']) == expected_ages
