class ColumnMapper:
    @staticmethod
    def map_columns_by_keywords_to_fields(df_columns, keywords):
        matched_columns = {}
        for field_name, key_list in keywords.items():
            matches = [
                column for column in df_columns
                if any(keyword in column.lower() for keyword in key_list)
            ]
            if len(matches) > 1:
                raise ValueError(f"Multiple matches found for '{field_name}': {matches}")
            elif not matches:
                raise ValueError(f"No column matched for field '{field_name}' with keywords {key_list}")
            else:
                matched_columns[field_name] = matches[0]
        return matched_columns
